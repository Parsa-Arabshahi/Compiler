class GraphvizExporter:

    def __init__(self, program):
        self.program = program

    def node_color(self, layer_type):

        colors = {

            "Linear": "lightblue",
            "Conv2d": "orange",

            "ReLU": "lightgreen",
            "GELU": "lightgreen",
            "Sigmoid": "lightgreen",
            "Tanh": "lightgreen",
            "LeakyReLU": "lightgreen",
            "ELU": "lightgreen",
            "Softmax": "lightgreen",

            "Dropout": "khaki",

            "BatchNorm2d": "plum",
            "LayerNorm": "plum",

            "Flatten": "gray90",

            "Concat": "gold",
            "Add": "gold",
            "Residual": "gold",

            "MultiHeadAttention": "tomato",
            "MultiHeadAttn": "tomato",

            "LSTM": "lightsalmon",
            "GRU": "lightsalmon"

        }

        return colors.get(layer_type, "white")

    def export(self):

        lines = []

        lines.append(f"digraph {self.program.model.name} {{")
        lines.append("    rankdir=LR;")
        lines.append("")

        #####################################################
        # Input
        #####################################################

        lines.append(
            f'    {self.program.model.input_name} '
            '[shape=oval, style=filled, fillcolor=lightgreen];'
        )

        #####################################################
        # آیا Output خودش یک Node است؟
        #####################################################

        output_is_node = any(

            node.id == self.program.model.output_name

            for node in self.program.nodes

        )

        if not output_is_node:

            lines.append(
                f'    {self.program.model.output_name} '
                '[shape=doublecircle, style=filled, fillcolor=lightblue];'
            )

        lines.append("")

        #####################################################
        # Nodes
        #####################################################

        for node in self.program.nodes:

            color = self.node_color(node.layer_type)

            if node.id == self.program.model.output_name:

                lines.append(
                    f'    {node.id} '
                    f'[label="{node.id}\\n{node.layer_type}", '
                    'shape=box, style=filled, '
                    f'fillcolor="{color}", penwidth=2];'
                )

            else:

                lines.append(
                    f'    {node.id} '
                    f'[label="{node.id}\\n{node.layer_type}", '
                    'shape=box, style=filled, '
                    f'fillcolor="{color}"];'
                )

        lines.append("")

        #####################################################
        # Edges
        #####################################################

        for edge in self.program.edges:

            if edge.label:

                lines.append(
                    f'    {edge.source} -> {edge.target} '
                    f'[label="{edge.label}"];'
                )

            else:

                lines.append(
                    f"    {edge.source} -> {edge.target};"
                )

        lines.append("}")

        return "\n".join(lines)