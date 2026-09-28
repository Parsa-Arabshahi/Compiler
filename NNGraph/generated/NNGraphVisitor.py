# Generated from NNGraph.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .NNGraphParser import NNGraphParser
else:
    from NNGraphParser import NNGraphParser

# This class defines a complete generic visitor for a parse tree produced by NNGraphParser.

class NNGraphVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by NNGraphParser#program.
    def visitProgram(self, ctx:NNGraphParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#modelDecl.
    def visitModelDecl(self, ctx:NNGraphParser.ModelDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#inputDecl.
    def visitInputDecl(self, ctx:NNGraphParser.InputDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#outputDecl.
    def visitOutputDecl(self, ctx:NNGraphParser.OutputDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#shape.
    def visitShape(self, ctx:NNGraphParser.ShapeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#graphDecl.
    def visitGraphDecl(self, ctx:NNGraphParser.GraphDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#graphStatement.
    def visitGraphStatement(self, ctx:NNGraphParser.GraphStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#nodeDecl.
    def visitNodeDecl(self, ctx:NNGraphParser.NodeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#edgeDecl.
    def visitEdgeDecl(self, ctx:NNGraphParser.EdgeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#edgeLabel.
    def visitEdgeLabel(self, ctx:NNGraphParser.EdgeLabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#parameterList.
    def visitParameterList(self, ctx:NNGraphParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#parameter.
    def visitParameter(self, ctx:NNGraphParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#value.
    def visitValue(self, ctx:NNGraphParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#tuple.
    def visitTuple(self, ctx:NNGraphParser.TupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#list.
    def visitList(self, ctx:NNGraphParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#configDecl.
    def visitConfigDecl(self, ctx:NNGraphParser.ConfigDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NNGraphParser#configEntry.
    def visitConfigEntry(self, ctx:NNGraphParser.ConfigEntryContext):
        return self.visitChildren(ctx)



del NNGraphParser