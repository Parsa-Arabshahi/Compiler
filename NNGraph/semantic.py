from collections import defaultdict, deque
from shape_inference import ShapeInference


class SemanticError(Exception):
    pass


class SemanticAnalyzer:

    def __init__(self, program):

        self.program = program

        self.nodes = {n.id: n for n in program.nodes}

        self.graph = defaultdict(list)

        self.indegree = defaultdict(int)

        self.reverse_graph = defaultdict(list)

    def analyze(self):

        self.check_duplicate_nodes()

        self.build_graph()

        self.check_undefined_nodes()

        self.check_node_inputs()

        self.check_cycles()

        self.check_reachability()

        self.check_output_exists()

        self.check_input_output()

        # run shape inference first so missing but inferable params get filled
        self.check_shapes_consistency()

        # now enforce required parameters (inferred ones are present)
        self.check_layer_parameters()

        self.check_parameter_types()

    def check_node_inputs(self):

        for node in self.program.nodes:

            normal = self.get_normal_inputs(node.id)

            residual = self.get_residual_inputs(node.id)

            ####################################################
            # Linear Layers
            ####################################################

            if node.layer_type in {

                "Linear",
                "Conv2d",
                "Dropout",
                "BatchNorm2d",
                "LayerNorm",
                "Flatten",
                "ReLU",
                "Sigmoid",
                "Tanh",
                "GELU",
                "ELU",
                "LeakyReLU",
                "Softmax",
                "LSTM",
                "GRU"

            }:

                if len(normal) != 1:
                    raise SemanticError(
                        f"{node.layer_type} node "
                        f"'{node.id}' must have exactly one normal input."
                    )

            ####################################################
            # Add
            ####################################################

            elif node.layer_type == "Add":

                if len(normal) < 2:
                    raise SemanticError(
                        f"Add node '{node.id}' needs at least two inputs."
                    )

            ####################################################
            # Concat
            ####################################################

            elif node.layer_type == "Concat":

                if len(normal) < 2:
                    raise SemanticError(
                        f"Concat node '{node.id}' needs at least two inputs."
                    )

            ####################################################
            # Residual
            ####################################################

            elif node.layer_type == "Residual":

                if len(normal) + len(residual) < 2:
                    raise SemanticError(
                        f"Residual node '{node.id}' needs at least two inputs."
                    )

            ####################################################
            # Attention
            ####################################################

            elif node.layer_type in {

                "MultiHeadAttention",
                "MultiHeadAttn"

            }:

                if len(normal) not in (1, 3):
                    raise SemanticError(
                        f"{node.layer_type} node "
                        f"'{node.id}' must have one input "
                        f"(self-attention) or three inputs "
                        f"(Q,K,V)."
                    )

            ####################################################
            # Split
            ####################################################

            elif node.layer_type == "Split":

                if len(normal) != 1:
                    raise SemanticError(
                        f"Split node '{node.id}' "
                        f"must have one input."
                    )


    def check_input_output(self):

        input_name = self.program.model.input_name

        output_name = self.program.model.output_name

        if input_name in self.nodes:
            raise SemanticError(
                "Input name conflicts with a node name."
            )

        if output_name == input_name:
            raise SemanticError(
                "Input and output cannot have the same name."
            )

    def check_duplicate_nodes(self):

        seen = set()

        for node in self.program.nodes:

            if node.id in seen:

                raise SemanticError(
                    f"Duplicate node id '{node.id}'"
                )

            seen.add(node.id)

    def build_graph(self):

        self.graph.clear()
        self.reverse_graph.clear()
        self.indegree.clear()

        for edge in self.program.edges:
            self.graph[edge.source].append(edge.target)

            self.reverse_graph[edge.target].append(edge.source)

            self.indegree[edge.target] += 1

    def check_undefined_nodes(self):

        valid = set(self.nodes.keys())

        valid.add(self.program.model.input_name)

        valid.add(self.program.model.output_name)

        for edge in self.program.edges:

            if edge.source not in valid:

                raise SemanticError(
                    f"Undefined node '{edge.source}'"
                )

            if edge.target not in valid:

                raise SemanticError(
                    f"Undefined node '{edge.target}'"
                )

    def check_cycles(self):

        indegree = dict(self.indegree)

        q = deque()

        vertices = set()

        vertices.add(self.program.model.input_name)

        vertices.add(self.program.model.output_name)

        vertices.update(self.nodes.keys())

        for v in vertices:

            indegree.setdefault(v, 0)

            if indegree[v] == 0:
                q.append(v)

        count = 0

        while q:

            u = q.popleft()

            count += 1

            for nxt in self.graph[u]:

                indegree[nxt] -= 1

                if indegree[nxt] == 0:

                    q.append(nxt)

        if count != len(vertices):

            raise SemanticError(
                "Graph contains a cycle."
            )

    def check_reachability(self):

        visited = set()

        q = deque()

        q.append(self.program.model.input_name)

        while q:

            u = q.popleft()

            if u in visited:
                continue

            visited.add(u)

            for nxt in self.graph[u]:

                q.append(nxt)

        for node in self.nodes:

            if node not in visited:

                raise SemanticError(
                    f"Node '{node}' is unreachable."
                )

    def check_output_exists(self):

        if self.program.model.output_name not in self.graph:

            incoming = False

            for e in self.program.edges:

                if e.target == self.program.model.output_name:
                    incoming = True

            if not incoming:

                raise SemanticError(
                    "Output node is never reached."
                )

    def check_layer_parameters(self):

        required = {

            "Linear": [
                "in_features",
                "out_features"
            ],

            "Conv2d": [
                "in_ch",
                "out_ch",
                "kernel"
            ],

            "Dropout": [
                "p"
            ],

            "Softmax": [
                "dim"
            ],

            "LayerNorm": [
                "normalized_shape"
            ]

        }

        for node in self.program.nodes:

            if node.layer_type not in required:
                continue

            for p in required[node.layer_type]:

                if p not in node.params:

                    raise SemanticError(

                        f"{node.layer_type} node '{node.id}' "

                        f"missing parameter '{p}'."

                    )

        allowed = {

            "Linear": {"in_features", "out_features"},

            "Conv2d": {
                "in_ch",
                "out_ch",
                "kernel",
                "stride",
                "padding"
            },

            "Dropout": {"p"},

            "Softmax": {"dim"},

            "LayerNorm": {"normalized_shape"},

            "BatchNorm2d": {"num_features"},

            "Flatten": {
                "start_dim",
                "end_dim"
            },

            "MultiHeadAttention": {
                "embed_dim",
                "num_heads"
            },

            "MultiHeadAttn": {
                "embed_dim",
                "num_heads"
            },

            "ReLU": set(),

            "GELU": set(),

            "Sigmoid": set(),

            "Tanh": set(),

            "ELU": set(),

            "LeakyReLU": set(),

            "Add": set(),

            "Concat": {"dim"},

            "Residual": set(),

            "Split": set(),

            "LSTM": {
                "input_size",
                "hidden_size",
                "num_layers"
            },

            "GRU": {
                "input_size",
                "hidden_size",
                "num_layers"
            }

        }

        for node in self.program.nodes:

            if node.layer_type not in allowed:
                continue

            for key in node.params:

                if key not in allowed[node.layer_type]:
                    raise SemanticError(

                        f"Unknown parameter '{key}' "
                        f"for layer '{node.layer_type}'."

                    )

    def check_shapes_consistency(self):

        infer = ShapeInference(self.program)
        infer.infer()

        shapes = infer.shapes

        def get_shape(name):
            return shapes.get(name)

        for node in self.program.nodes:

            parents = self.get_normal_inputs(node.id)

            parent_shapes = [get_shape(p) for p in parents if get_shape(p) is not None]

            if not parent_shapes and node.layer_type not in ("Linear",):
                continue

            if node.layer_type == "Linear":

                if not parents:
                    continue

                parent_shape = get_shape(parents[0])

                if parent_shape is None:
                    continue

                expected_in = parent_shape[-1]

                if "in_features" in node.params:
                    actual = node.params["in_features"]

                    if not isinstance(actual, int):
                        raise SemanticError(f"Linear.in_features for node '{node.id}' must be int.")

                    if actual != expected_in:
                        raise SemanticError(
                            f"Linear node '{node.id}' has in_features={actual}, but parent provides {expected_in}."
                        )

            elif node.layer_type == "Conv2d":

                if not parents:
                    continue

                parent_shape = get_shape(parents[0])

                if parent_shape is None or len(parent_shape) < 3:
                    raise SemanticError(f"Conv2d node '{node.id}' expects input shape (C,H,W).")

                in_ch = node.params.get("in_ch")
                out_ch = node.params.get("out_ch")
                kernel = node.params.get("kernel")
                stride = node.params.get("stride", 1)
                padding = node.params.get("padding", 0)

                if in_ch is None or out_ch is None or kernel is None:
                    raise SemanticError(f"Conv2d node '{node.id}' missing required params.")

                if parent_shape[0] != in_ch:
                    raise SemanticError(
                        f"Conv2d node '{node.id}' in_ch={in_ch} but parent channels={parent_shape[0]}."
                    )

                c, h, w = parent_shape[0], parent_shape[1], parent_shape[2]

                try:
                    out_h = (h + 2 * padding - kernel) // stride + 1
                    out_w = (w + 2 * padding - kernel) // stride + 1
                except Exception:
                    raise SemanticError(f"Conv2d node '{node.id}' has invalid kernel/stride/padding.")

                if out_h <= 0 or out_w <= 0:
                    raise SemanticError(f"Conv2d node '{node.id}' produces invalid output spatial size.")

                shapes[node.id] = (out_ch, out_h, out_w)

            elif node.layer_type == "BatchNorm2d":

                if not parents:
                    continue

                parent_shape = get_shape(parents[0])

                if parent_shape is None or len(parent_shape) < 1:
                    raise SemanticError(f"BatchNorm2d node '{node.id}' expects channel dimension.")

                num = node.params.get("num_features")

                if num is None:
                    raise SemanticError(f"BatchNorm2d node '{node.id}' missing num_features.")

                if parent_shape[0] != num:
                    raise SemanticError(
                        f"BatchNorm2d node '{node.id}' num_features={num} but parent channels={parent_shape[0]}."
                    )

                shapes[node.id] = parent_shape

            elif node.layer_type == "LayerNorm":

                if not parents:
                    continue

                parent_shape = get_shape(parents[0])

                if parent_shape is None:
                    continue

                norm = node.params.get("normalized_shape")

                if norm is None:
                    raise SemanticError(f"LayerNorm node '{node.id}' missing normalized_shape.")

                if isinstance(norm, tuple):
                    tail = parent_shape[-len(norm):]
                    if tuple(tail) != norm:
                        raise SemanticError(
                            f"LayerNorm node '{node.id}' normalized_shape={norm} incompatible with parent shape {parent_shape}."
                        )
                else:
                    if parent_shape[-1] != norm:
                        raise SemanticError(
                            f"LayerNorm node '{node.id}' normalized_shape={norm} incompatible with parent last-dim {parent_shape[-1]}."
                        )

                shapes[node.id] = parent_shape

            elif node.layer_type == "Flatten":

                if not parents:
                    continue

                parent_shape = get_shape(parents[0])

                if parent_shape is None:
                    continue

                start = node.params.get("start_dim", 0)
                end = node.params.get("end_dim", len(parent_shape) - 1)

                if start < 0:
                    start = len(parent_shape) + start
                if end < 0:
                    end = len(parent_shape) + end

                if not (0 <= start <= end < len(parent_shape)):
                    raise SemanticError(f"Flatten node '{node.id}' has invalid start_dim/end_dim.")

                flattened = 1
                for d in parent_shape[start:end + 1]:
                    flattened *= d

                new_shape = parent_shape[:start] + (flattened,) + parent_shape[end + 1:]

                shapes[node.id] = new_shape

            elif node.layer_type == "Concat":

                dim = node.params.get("dim")

                if dim is None:
                    raise SemanticError(f"Concat node '{node.id}' missing dim parameter.")

                if not parent_shapes:
                    continue

                if len(parent_shapes) != len(parents):
                    raise SemanticError(f"Concat node '{node.id}' has missing parent shapes.")

                base = parent_shapes[0]

                # normalize dim: support negative and common 1-based conventions
                if dim < 0:
                    dim = len(base) + dim
                elif len(base) == 3 and dim == 1:
                    # user likely specified PyTorch-style dim=1 for channels (batch,C,H,W)
                    dim = 0

                if not (0 <= dim < len(base)):
                    raise SemanticError(f"Concat node '{node.id}' dim={node.params.get('dim')} out of range for parent rank {len(base)}.")

                for ps in parent_shapes[1:]:
                    if len(ps) != len(base):
                        raise SemanticError(f"Concat node '{node.id}' parents rank mismatch.")
                    for i in range(len(base)):
                        if i == dim:
                            continue
                        if ps[i] != base[i]:
                            raise SemanticError(f"Concat node '{node.id}' non-concat dims must match.")

                summed = sum(ps[dim] for ps in parent_shapes)

                new_shape = list(base)
                new_shape[dim] = summed
                shapes[node.id] = tuple(new_shape)

            elif node.layer_type in {"Add", "Residual"}:

                if not parent_shapes:
                    continue

                first = parent_shapes[0]

                for ps in parent_shapes[1:]:
                    if ps != first:
                        raise SemanticError(f"{node.layer_type} node '{node.id}' has mismatched input shapes.")

                shapes[node.id] = first

            elif node.layer_type in {"MultiHeadAttention", "MultiHeadAttn"}:

                if not parents:
                    continue

                parent_shape = get_shape(parents[0])

                if parent_shape is None:
                    continue

                embed = node.params.get("embed_dim")

                if embed is None:
                    raise SemanticError(f"{node.layer_type} node '{node.id}' missing embed_dim.")

                if parent_shape[-1] != embed:
                    raise SemanticError(
                        f"{node.layer_type} node '{node.id}' embed_dim={embed} incompatible with parent last-dim {parent_shape[-1]}."
                    )

                shapes[node.id] = parent_shape

            elif node.layer_type in {"LSTM", "GRU"}:

                if not parents:
                    continue

                parent_shape = get_shape(parents[0])

                if parent_shape is None:
                    continue

                inp = node.params.get("input_size")

                if inp is None:
                    raise SemanticError(f"{node.layer_type} node '{node.id}' missing input_size.")

                if parent_shape[-1] != inp:
                    raise SemanticError(
                        f"{node.layer_type} node '{node.id}' input_size={inp} incompatible with parent last-dim {parent_shape[-1]}."
                    )

                shapes[node.id] = parent_shape

        # Final pass: ensure nodes that require tensor shapes have inferred shapes
        required_shape_types = {
            "Linear",
            "Conv2d",
            "BatchNorm2d",
            "LayerNorm",
            "Flatten",
            "Concat",
            "Add",
            "Residual",
            "MultiHeadAttention",
            "MultiHeadAttn",
            "LSTM",
            "GRU"
        }

        for node in self.program.nodes:
            if node.layer_type in required_shape_types:
                if node.id not in shapes:
                    raise SemanticError(
                        f"Cannot infer shape for node '{node.id}' of type '{node.layer_type}'."
                    )
    
    def check_parameter_types(self):

        for node in self.program.nodes:

            p = node.params

            if node.layer_type == "Linear":

                if not isinstance(p["in_features"], int):
                    raise SemanticError(
                        "Linear.in_features must be int."
                    )
                # if "in_features" in p:
                #
                #     if not isinstance(
                #             p["in_features"],
                #             int
                #     ):
                #         raise SemanticError(
                #             "Linear.in_features must be int."
                #         )

                if not isinstance(p["out_features"], int):
                    raise SemanticError(
                        "Linear.out_features must be int."
                    )

            elif node.layer_type == "Dropout":

                if not isinstance(p["p"], (int, float)):
                    raise SemanticError(
                        "Dropout.p must be numeric."
                    )

                if not (0 <= p["p"] <= 1):
                    raise SemanticError(
                        "Dropout.p must be in [0,1]."
                    )

            elif node.layer_type == "Softmax":

                if not isinstance(p["dim"], int):
                    raise SemanticError(
                        "Softmax.dim must be int."
                    )

            elif node.layer_type == "Flatten":

                if "start_dim" in p and \
                        not isinstance(p["start_dim"], int):
                    raise SemanticError(
                        "Flatten.start_dim must be int."
                    )

                if "end_dim" in p and \
                        not isinstance(p["end_dim"], int):
                    raise SemanticError(
                        "Flatten.end_dim must be int."
                    )

    def get_normal_inputs(self, node_id):

        inputs = []

        for edge in self.program.edges:

            if edge.target != node_id:
                continue

            if edge.label is None:
                inputs.append(edge.source)

        return inputs

    def get_residual_inputs(self, node_id):

        inputs = []

        residual_keywords = (
            "residual",
            "shortcut",
            "skip",
            "identity"
        )

        for edge in self.program.edges:

            if edge.target != node_id:
                continue

            if edge.label is None:
                continue

            label = edge.label.lower()

            if any(k in label for k in residual_keywords):
                inputs.append(edge.source)

        return inputs
