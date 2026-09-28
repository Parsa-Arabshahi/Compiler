from generated.NNGraphVisitor import NNGraphVisitor
from ast_nodes import *


class ASTBuilder(NNGraphVisitor):

    def __init__(self):
        super().__init__()

        self.nodes = []
        self.edges = []
        self.config = {}

    # -------------------------------------------------

    def visitProgram(self, ctx):

        model = self.visit(ctx.modelDecl())

        if ctx.graphDecl():
            self.visit(ctx.graphDecl())

        if ctx.configDecl():
            self.visit(ctx.configDecl())

        return Program(
            model=model,
            nodes=self.nodes,
            edges=self.edges,
            config=Config(self.config)
        )

    # -------------------------------------------------

    def visitModelDecl(self, ctx):

        model_name = ctx.ID().getText()

        input_ctx = ctx.inputDecl()
        output_ctx = ctx.outputDecl()

        input_name = input_ctx.ID().getText()

        shape = tuple(
            int(x.getText())
            for x in input_ctx.shape().INT()
        )

        output_name = output_ctx.ID().getText()

        return Model(
            model_name,
            input_name,
            shape,
            output_name
        )

    # -------------------------------------------------

    def visitGraphDecl(self, ctx):

        for stmt in ctx.graphStatement():
            self.visit(stmt)

    # -------------------------------------------------

    def visitGraphStatement(self, ctx):

        return self.visitChildren(ctx)

    # -------------------------------------------------

    def visitNodeDecl(self, ctx):

        node = Node(

            id=ctx.ID(0).getText(),

            layer_type=ctx.ID(1).getText(),

            params=self.visit(ctx.parameterList())
            if ctx.parameterList()
            else {}

        )

        self.nodes.append(node)

        return node

    # -------------------------------------------------

    def visitEdgeDecl(self, ctx):

        src = ctx.ID(0).getText()
        dst = ctx.ID(1).getText()

        label = None

        if ctx.edgeLabel():
            label = self.visit(ctx.edgeLabel())

        print(src, "->", dst, "label =", label)

        edge = Edge(src, dst, label)

        self.edges.append(edge)

        return edge

    # -------------------------------------------------

    def visitEdgeLabel(self, ctx):

        text = ctx.STRING().getText()

        return text[1:-1]

    # -------------------------------------------------

    def visitParameterList(self, ctx):

        result = {}

        for p in ctx.parameter():
            k, v = self.visit(p)

            result[k] = v

        return result

    # -------------------------------------------------

    def visitParameter(self, ctx):

        name = ctx.ID().getText()

        value = self.visit(ctx.value())

        return name, value

    # -------------------------------------------------

    def visitValue(self, ctx):

        if ctx.INT():
            return int(ctx.INT().getText())

        if ctx.FLOAT():
            return float(ctx.FLOAT().getText())

        if ctx.STRING():
            return ctx.STRING().getText()[1:-1]

        if ctx.BOOL():
            text = ctx.BOOL().getText().lower()

            return text == "true"

        if ctx.NONE():
            return None

        if ctx.tuple_():
            return self.visit(ctx.tuple_())

        if hasattr(ctx, "list") and ctx.list():
            return self.visit(ctx.list())

        return None

    # -------------------------------------------------
    def visitList(self, ctx):

        result = []

        for v in ctx.value():
            result.append(self.visit(v))

        return result

    def visitTuple(self, ctx):

        return tuple(

            self.visit(v)

            for v in ctx.value()

        )

    # -------------------------------------------------

    def visitConfigDecl(self, ctx):

        for entry in ctx.configEntry():

            key, value = self.visit(entry)

            self.config[key] = value

    # -------------------------------------------------

    def visitConfigEntry(self, ctx):

        key = ctx.ID().getText()

        value = self.visit(ctx.value())

        return key, value