from collections import defaultdict


class ShapeInference:

    def __init__(self, program):

        self.program = program

        self.shapes = {}

        self.parents = defaultdict(list)

        self.node_map = {
            node.id: node
            for node in program.nodes
        }

        for edge in program.edges:
            self.parents[edge.target].append(edge.source)

    ########################################################

    def infer(self):

        # شکل ورودی مدل
        self.shapes[
            self.program.model.input_name
        ] = tuple(self.program.model.input_shape)

        changed = True

        while changed:

            changed = False

            for node in self.program.nodes:

                if node.id in self.shapes:
                    continue

                if self.try_infer(node):

                    changed = True

        return self.program

    ########################################################

    def try_infer(self, node):

        if node.id not in self.parents:
            return False

        parents = self.parents[node.id]

        # require all parent shapes available for multi-input nodes
        parent_shapes = []
        for p in parents:
            if p not in self.shapes:
                return False
            parent_shapes.append(self.shapes[p])

        # for single-input nodes, use the first parent
        parent = parents[0]
        parent_shape = self.shapes[parent]

        ####################################################
        # Linear
        ####################################################

        if node.layer_type == "Linear":

            # اگر کاربر ننوشته باشد
            if "in_features" not in node.params:
                node.params["in_features"] = parent_shape[-1]
                print(f"[Infer] {node.id}: in_features = {parent_shape[-1]}")
            out_features = node.params["out_features"]

            # preserve leading dims (e.g., batch or sequence dims)
            if len(parent_shape) == 1:
                self.shapes[node.id] = (out_features,)
            else:
                self.shapes[node.id] = parent_shape[:-1] + (out_features,)

            return True

        ####################################################
        # Layers that preserve shape
        ####################################################

        elif node.layer_type in {

            "ReLU",
            "Sigmoid",
            "Tanh",
            "GELU",
            "ELU",
            "LeakyReLU",
            "Dropout",
            "BatchNorm2d",
            "LayerNorm",
            "MultiHeadAttention",
            "MultiHeadAttn",
            "Softmax"

        }:

            self.shapes[node.id] = parent_shape

            return True
        ####################################################
        # Conv2d
        ####################################################

        if node.layer_type == "Conv2d":

            # expect parent shape (C,H,W)
            if parent_shape is None or len(parent_shape) < 3:
                return False

            in_ch = node.params.get("in_ch")
            out_ch = node.params.get("out_ch")
            kernel = node.params.get("kernel")
            stride = node.params.get("stride", 1)
            padding = node.params.get("padding", 0)

            if kernel is None or out_ch is None:
                return False

            # infer in_ch if missing
            if in_ch is None:
                node.params["in_ch"] = parent_shape[0]
                in_ch = parent_shape[0]
                print(f"[Infer] {node.id}: in_ch = {in_ch}")

            # compute output spatial dims
            c, h, w = parent_shape[0], parent_shape[1], parent_shape[2]

            try:
                out_h = (h + 2 * padding - kernel) // stride + 1
                out_w = (w + 2 * padding - kernel) // stride + 1
            except Exception:
                return False

            self.shapes[node.id] = (out_ch, out_h, out_w)

            return True

        ####################################################
        # BatchNorm2d
        ####################################################

        if node.layer_type == "BatchNorm2d":

            # require parent shape
            if parent_shape is None or len(parent_shape) < 1:
                return False

            # infer num_features if missing
            if "num_features" not in node.params:
                node.params["num_features"] = parent_shape[0]
                print(f"[Infer] {node.id}: num_features = {parent_shape[0]}")

            self.shapes[node.id] = parent_shape

            return True

        ####################################################
        # LayerNorm
        ####################################################

        if node.layer_type == "LayerNorm":

            if parent_shape is None:
                return False

            self.shapes[node.id] = parent_shape

            return True

        ####################################################
        # Flatten
        ####################################################

        if node.layer_type == "Flatten":

            if parent_shape is None:
                return False

            start = node.params.get("start_dim", 0)
            end = node.params.get("end_dim", len(parent_shape) - 1)

            if start < 0:
                start = len(parent_shape) + start
            if end < 0:
                end = len(parent_shape) + end

            if not (0 <= start <= end < len(parent_shape)):
                return False

            flattened = 1
            for d in parent_shape[start:end + 1]:
                flattened *= d

            new_shape = parent_shape[:start] + (flattened,) + parent_shape[end + 1:]

            self.shapes[node.id] = new_shape

            return True

        ####################################################
        # Concat
        ####################################################

        if node.layer_type == "Concat":

            # need all parent shapes
            if not parent_shapes:
                return False

            dim = node.params.get("dim")
            if dim is None:
                return False

            base = parent_shapes[0]

            if dim < 0:
                dim = len(base) + dim

            for ps in parent_shapes[1:]:
                if len(ps) != len(base):
                    return False
                for i in range(len(base)):
                    if i == dim:
                        continue
                    if ps[i] != base[i]:
                        return False

            summed = sum(ps[dim] for ps in parent_shapes)
            new_shape = list(base)
            new_shape[dim] = summed

            self.shapes[node.id] = tuple(new_shape)

            return True

        ####################################################
        # Add / Residual
        ####################################################

        if node.layer_type in {"Add", "Residual"}:

            if not parent_shapes:
                return False

            first = parent_shapes[0]
            for ps in parent_shapes[1:]:
                if ps != first:
                    return False

            self.shapes[node.id] = first

            return True
        ####################################################
        # هنوز چیزی پیاده نشده
        ####################################################

        return False