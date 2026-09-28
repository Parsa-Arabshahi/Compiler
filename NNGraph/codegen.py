from collections import defaultdict, deque
from ast_nodes import *


class CodeGenerator:

    def __init__(self, program):

        self.program = program

        self.lines = []

        # Graph
        self.graph = defaultdict(list)

        # Reverse Graph
        self.parents = defaultdict(list)

        # Indegree
        self.indegree = defaultdict(int)

        # id -> Node
        self.node_map = {}

        for node in program.nodes:
            self.node_map[node.id] = node

    LAYER_MAP = {

        "Linear":
            lambda p:
                f"nn.Linear("
                f"in_features={p['in_features']}, "
                f"out_features={p['out_features']})",

        "Conv2d":
            lambda p:
                f"nn.Conv2d("
                f"in_channels={p['in_ch']}, "
                f"out_channels={p['out_ch']}, "
                f"kernel_size={p['kernel']}, "
                f"stride={p.get('stride',1)}, "
                f"padding={p.get('padding',0)})",

        "ReLU":
            lambda p:
                "nn.ReLU()",

        "Sigmoid":
            lambda p:
                "nn.Sigmoid()",

        "Tanh":
            lambda p:
                "nn.Tanh()",

        "Dropout":
            lambda p:
                f"nn.Dropout(p={p['p']})",

        "Softmax":
            lambda p:
                f"nn.Softmax(dim={p['dim']})",

        "Flatten":
            lambda p:
                (
                    f"nn.Flatten("
                    f"start_dim={p.get('start_dim',1)}, "
                    f"end_dim={p.get('end_dim',-1)})"
                ),

        "LayerNorm":
            lambda p:
                f"nn.LayerNorm({p['normalized_shape']})",

        # فعلاً Placeholder
        "Residual":
            lambda p:
                "nn.Identity()",

        "Concat":
            lambda p:
                "nn.Identity()",

        "Split":
            lambda p:
                "nn.Identity()",

        "Add":
            lambda p:
                "nn.Identity()",

        "BatchNorm2d":
            lambda p:
                f"nn.BatchNorm2d({p['num_features']})",

        "MaxPool2d":
            lambda p:
                f"nn.MaxPool2d("
                f"{p['kernel_size']}, "
                f"stride={p.get('stride',None)})",

        "AvgPool2d":
            lambda p:
                f"nn.AvgPool2d("
                f"{p['kernel_size']}, "
                f"stride={p.get('stride',None)})",

        "Embedding":
            lambda p:
                f"nn.Embedding("
                f"{p['num_embeddings']}, "
                f"{p['embedding_dim']})",

        "GELU":
            lambda p:
                "nn.GELU()",

        "ELU":
            lambda p:
                "nn.ELU()",

        "LeakyReLU":
            lambda p:
                f"nn.LeakyReLU("
                f"negative_slope={p.get('negative_slope',0.01)})",

        "LSTM":
            lambda p:
                f"nn.LSTM("
                f"input_size={p['input_size']}, "
                f"hidden_size={p['hidden_size']}, "
                f"batch_first=True)",

        "GRU":
            lambda p:
                f"nn.GRU("
                f"input_size={p['input_size']}, "
                f"hidden_size={p['hidden_size']}, "
                f"batch_first=True)",

        "MultiHeadAttention":
            lambda p:
                f"nn.MultiheadAttention("
                f"embed_dim={p['embed_dim']}, "
                f"num_heads={p['num_heads']}, "
                f"batch_first=True)"
    }
    def emit(self, line=""):

        self.lines.append(line)

    def generate(self):

        self.build_graph()

        self.generate_imports()

        self.generate_class()

        return "\n".join(self.lines)

    def build_graph(self):

        self.graph.clear()
        self.parents.clear()
        self.indegree.clear()

        for edge in self.program.edges:
            self.graph[edge.source].append(edge.target)

            self.parents[edge.target].append((edge.source,edge.label))

            self.indegree[edge.target] += 1

        self.indegree.setdefault(
            self.program.model.input_name,
            0
        )

        for node in self.program.nodes:
            self.indegree.setdefault(node.id, 0)

    def topological_sort(self):

        indegree = dict(self.indegree)

        q = deque()

        for v in indegree:

            if indegree[v] == 0:
                q.append(v)

        order = []

        while q:

            u = q.popleft()

            order.append(u)

            for nxt in self.graph[u]:

                indegree[nxt] -= 1

                if indegree[nxt] == 0:
                    q.append(nxt)

        return order

    def generate_imports(self):
        self.emit("import torch")
        self.emit("import torch.nn as nn")
        self.emit("")

    def generate_class(self):

        model = self.program.model.name

        self.emit(f"class {model}(nn.Module):")

        self.emit("")

        self.generate_init()

        self.emit("")

        self.generate_forward()

        self.emit("")

        self.generate_main()

    def generate_init(self):

        model = self.program.model.name

        self.emit("    def __init__(self):")

        self.emit(
            f"        super({model}, self).__init__()"
        )

        self.emit("")

        self.generate_layers()

    def layer_to_code(self, node):

        if node.layer_type not in self.LAYER_MAP:
            raise Exception(
                f"Unsupported layer '{node.layer_type}'"
            )
        elif node.layer_type == "LayerNorm":

            shape = node.params["normalized_shape"]

            if isinstance(shape, tuple) and len(shape) == 1:
                shape = shape[0]

            return f"nn.LayerNorm({shape})"

        return self.LAYER_MAP[node.layer_type](node.params)

    def generate_layers(self):

        for node in self.program.nodes:
            code = self.layer_to_code(node)

            self.emit(
                f"        self.{node.id} = {code}"
            )

    def generate_forward(self):

        input_name = self.program.model.input_name
        output_name = self.program.model.output_name

        order = self.topological_sort()

        self.emit(f"    def forward(self, {input_name}):")

        values = {
            input_name: input_name
        }

        for node_id in order:

            # ورودی مدل
            if node_id == input_name:
                continue

            # اگر رأس لایه نیست
            if node_id not in self.node_map:
                continue

            node = self.node_map[node_id]

            parents = self.parents.get(node_id, [])

            if len(parents) == 0:
                raise Exception(
                    f"Node '{node_id}' has no input."
                )

            normal_inputs = []
            residual_inputs = []

            for parent, label in parents:

                if parent not in values:
                    raise Exception(
                        f"Parent '{parent}' of '{node_id}' has not been computed."
                    )

                if (
                        label is not None and
                        any(
                            k in label.lower()
                            for k in (
                                    "residual",
                                    "shortcut",
                                    "skip",
                                    "identity"
                            )
                        )
                ):

                    residual_inputs.append(values[parent])

                else:

                    normal_inputs.append(values[parent])

            ####################################################
            # Build Expression
            ####################################################

            # ---------- Concat ----------
            if node.layer_type == "Concat":

                dim = node.params.get("dim", 1)

                expr = (
                    f"torch.cat([{', '.join(normal_inputs)}], dim={dim})"
                )

            # ---------- Add ----------
            elif node.layer_type == "Add":

                expr = " + ".join(
                    normal_inputs + residual_inputs
                )

            # ---------- Residual ----------
            elif node.layer_type == "Residual":

                expr = " + ".join(
                    normal_inputs + residual_inputs
                )

            # ---------- Split ----------
            elif node.layer_type == "Split":

                expr = normal_inputs[0]

            # ---------- MultiHeadAttention ----------
            elif node.layer_type in (
                    "MultiHeadAttention",
                    "MultiHeadAttn"
            ):

                if len(normal_inputs) == 1:

                    x = normal_inputs[0]

                    expr = (
                        f"self.{node_id}"
                        f"({x}, {x}, {x})[0]"
                    )

                elif len(normal_inputs) == 3:

                    expr = (
                        f"self.{node_id}"
                        f"({normal_inputs[0]}, "
                        f"{normal_inputs[1]}, "
                        f"{normal_inputs[2]})[0]"
                    )

                else:

                    raise Exception(
                        f"{node.layer_type} expects 1 or 3 inputs."
                    )

            # ---------- LSTM ----------
            elif node.layer_type == "LSTM":

                expr = (
                    f"self.{node_id}"
                    f"({normal_inputs[0]})[0]"
                )

            # ---------- GRU ----------
            elif node.layer_type == "GRU":

                expr = (
                    f"self.{node_id}"
                    f"({normal_inputs[0]})[0]"
                )

            # ---------- Normal Layers ----------
            else:

                x = normal_inputs[0]

                if residual_inputs:
                    x = " + ".join(
                        [x] + residual_inputs
                    )

                expr = f"self.{node_id}({x})"

            ####################################################

            self.emit(
                f"        {node_id} = {expr}"
            )

            values[node_id] = node_id

        ########################################################

        self.emit("")

        # اگر خود output یک Node باشد
        if output_name in values:

            self.emit(
                f"        return {values[output_name]}"
            )

        # اگر output فقط یک نام باشد
        elif output_name in self.parents:

            parent = self.parents[output_name][0][0]

            self.emit(
                f"        return {values[parent]}"
            )

        # آخرین Node
        else:

            last = None

            for node_id in reversed(order):

                if node_id in values:
                    last = node_id

                    break

            self.emit(
                f"        return {values[last]}"
            )

    def generate_main(self):

        batch = self.program.config.values.get("batch_size", 1)

        device = self.program.config.values.get("device", "cpu")

        model = self.program.model.name

        shape = ", ".join(
            str(x)
            for x in self.program.model.input_shape
        )

        self.emit("")

        self.emit("if __name__ == '__main__':")

        self.emit(f"    device = torch.device('{device}')")

        self.emit(f"    model = {model}().to(device)")

        self.emit(
            f"    x = torch.randn({batch}, {shape}).to(device)"
        )

        self.emit("")

        self.emit("    y = model(x)")

        self.emit("")

        self.emit("    print(y)")

        self.emit("    print(y.shape)")
