# Generated from NNGraph.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .NNGraphParser import NNGraphParser
else:
    from NNGraphParser import NNGraphParser

# This class defines a complete listener for a parse tree produced by NNGraphParser.
class NNGraphListener(ParseTreeListener):

    # Enter a parse tree produced by NNGraphParser#program.
    def enterProgram(self, ctx:NNGraphParser.ProgramContext):
        pass

    # Exit a parse tree produced by NNGraphParser#program.
    def exitProgram(self, ctx:NNGraphParser.ProgramContext):
        pass


    # Enter a parse tree produced by NNGraphParser#modelDecl.
    def enterModelDecl(self, ctx:NNGraphParser.ModelDeclContext):
        pass

    # Exit a parse tree produced by NNGraphParser#modelDecl.
    def exitModelDecl(self, ctx:NNGraphParser.ModelDeclContext):
        pass


    # Enter a parse tree produced by NNGraphParser#inputDecl.
    def enterInputDecl(self, ctx:NNGraphParser.InputDeclContext):
        pass

    # Exit a parse tree produced by NNGraphParser#inputDecl.
    def exitInputDecl(self, ctx:NNGraphParser.InputDeclContext):
        pass


    # Enter a parse tree produced by NNGraphParser#outputDecl.
    def enterOutputDecl(self, ctx:NNGraphParser.OutputDeclContext):
        pass

    # Exit a parse tree produced by NNGraphParser#outputDecl.
    def exitOutputDecl(self, ctx:NNGraphParser.OutputDeclContext):
        pass


    # Enter a parse tree produced by NNGraphParser#shape.
    def enterShape(self, ctx:NNGraphParser.ShapeContext):
        pass

    # Exit a parse tree produced by NNGraphParser#shape.
    def exitShape(self, ctx:NNGraphParser.ShapeContext):
        pass


    # Enter a parse tree produced by NNGraphParser#graphDecl.
    def enterGraphDecl(self, ctx:NNGraphParser.GraphDeclContext):
        pass

    # Exit a parse tree produced by NNGraphParser#graphDecl.
    def exitGraphDecl(self, ctx:NNGraphParser.GraphDeclContext):
        pass


    # Enter a parse tree produced by NNGraphParser#graphStatement.
    def enterGraphStatement(self, ctx:NNGraphParser.GraphStatementContext):
        pass

    # Exit a parse tree produced by NNGraphParser#graphStatement.
    def exitGraphStatement(self, ctx:NNGraphParser.GraphStatementContext):
        pass


    # Enter a parse tree produced by NNGraphParser#nodeDecl.
    def enterNodeDecl(self, ctx:NNGraphParser.NodeDeclContext):
        pass

    # Exit a parse tree produced by NNGraphParser#nodeDecl.
    def exitNodeDecl(self, ctx:NNGraphParser.NodeDeclContext):
        pass


    # Enter a parse tree produced by NNGraphParser#edgeDecl.
    def enterEdgeDecl(self, ctx:NNGraphParser.EdgeDeclContext):
        pass

    # Exit a parse tree produced by NNGraphParser#edgeDecl.
    def exitEdgeDecl(self, ctx:NNGraphParser.EdgeDeclContext):
        pass


    # Enter a parse tree produced by NNGraphParser#edgeLabel.
    def enterEdgeLabel(self, ctx:NNGraphParser.EdgeLabelContext):
        pass

    # Exit a parse tree produced by NNGraphParser#edgeLabel.
    def exitEdgeLabel(self, ctx:NNGraphParser.EdgeLabelContext):
        pass


    # Enter a parse tree produced by NNGraphParser#parameterList.
    def enterParameterList(self, ctx:NNGraphParser.ParameterListContext):
        pass

    # Exit a parse tree produced by NNGraphParser#parameterList.
    def exitParameterList(self, ctx:NNGraphParser.ParameterListContext):
        pass


    # Enter a parse tree produced by NNGraphParser#parameter.
    def enterParameter(self, ctx:NNGraphParser.ParameterContext):
        pass

    # Exit a parse tree produced by NNGraphParser#parameter.
    def exitParameter(self, ctx:NNGraphParser.ParameterContext):
        pass


    # Enter a parse tree produced by NNGraphParser#value.
    def enterValue(self, ctx:NNGraphParser.ValueContext):
        pass

    # Exit a parse tree produced by NNGraphParser#value.
    def exitValue(self, ctx:NNGraphParser.ValueContext):
        pass


    # Enter a parse tree produced by NNGraphParser#tuple.
    def enterTuple(self, ctx:NNGraphParser.TupleContext):
        pass

    # Exit a parse tree produced by NNGraphParser#tuple.
    def exitTuple(self, ctx:NNGraphParser.TupleContext):
        pass


    # Enter a parse tree produced by NNGraphParser#list.
    def enterList(self, ctx:NNGraphParser.ListContext):
        pass

    # Exit a parse tree produced by NNGraphParser#list.
    def exitList(self, ctx:NNGraphParser.ListContext):
        pass


    # Enter a parse tree produced by NNGraphParser#configDecl.
    def enterConfigDecl(self, ctx:NNGraphParser.ConfigDeclContext):
        pass

    # Exit a parse tree produced by NNGraphParser#configDecl.
    def exitConfigDecl(self, ctx:NNGraphParser.ConfigDeclContext):
        pass


    # Enter a parse tree produced by NNGraphParser#configEntry.
    def enterConfigEntry(self, ctx:NNGraphParser.ConfigEntryContext):
        pass

    # Exit a parse tree produced by NNGraphParser#configEntry.
    def exitConfigEntry(self, ctx:NNGraphParser.ConfigEntryContext):
        pass



del NNGraphParser