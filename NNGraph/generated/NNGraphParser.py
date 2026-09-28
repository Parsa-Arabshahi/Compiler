# Generated from NNGraph.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,29,179,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,1,0,1,0,3,0,38,8,0,1,0,1,0,1,0,
        3,0,43,8,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,3,2,62,8,2,1,3,1,3,1,3,3,3,67,8,3,1,4,1,4,1,4,5,4,
        72,8,4,10,4,12,4,75,9,4,1,5,1,5,1,5,5,5,80,8,5,10,5,12,5,83,9,5,
        1,5,1,5,1,6,1,6,3,6,89,8,6,1,6,1,6,3,6,93,8,6,3,6,95,8,6,1,7,1,7,
        1,7,1,7,1,7,1,7,3,7,103,8,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,3,8,112,
        8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,5,10,123,8,10,10,10,12,
        10,126,9,10,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,
        12,3,12,139,8,12,1,13,1,13,1,13,1,13,5,13,145,8,13,10,13,12,13,148,
        9,13,1,13,1,13,1,14,1,14,1,14,1,14,5,14,156,8,14,10,14,12,14,159,
        9,14,1,14,1,14,1,15,1,15,1,15,5,15,166,8,15,10,15,12,15,169,9,15,
        1,15,1,15,1,16,1,16,1,16,1,16,3,16,177,8,16,1,16,0,0,17,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,28,30,32,0,0,183,0,34,1,0,0,0,2,46,
        1,0,0,0,4,53,1,0,0,0,6,63,1,0,0,0,8,68,1,0,0,0,10,76,1,0,0,0,12,
        94,1,0,0,0,14,96,1,0,0,0,16,106,1,0,0,0,18,113,1,0,0,0,20,119,1,
        0,0,0,22,127,1,0,0,0,24,138,1,0,0,0,26,140,1,0,0,0,28,151,1,0,0,
        0,30,162,1,0,0,0,32,172,1,0,0,0,34,42,3,2,1,0,35,37,3,10,5,0,36,
        38,3,30,15,0,37,36,1,0,0,0,37,38,1,0,0,0,38,43,1,0,0,0,39,40,3,30,
        15,0,40,41,3,10,5,0,41,43,1,0,0,0,42,35,1,0,0,0,42,39,1,0,0,0,43,
        44,1,0,0,0,44,45,5,0,0,1,45,1,1,0,0,0,46,47,5,1,0,0,47,48,5,23,0,
        0,48,49,5,19,0,0,49,50,3,4,2,0,50,51,3,6,3,0,51,52,5,20,0,0,52,3,
        1,0,0,0,53,54,5,4,0,0,54,55,5,23,0,0,55,56,5,14,0,0,56,57,5,8,0,
        0,57,58,5,17,0,0,58,59,3,8,4,0,59,61,5,18,0,0,60,62,5,16,0,0,61,
        60,1,0,0,0,61,62,1,0,0,0,62,5,1,0,0,0,63,64,5,5,0,0,64,66,5,23,0,
        0,65,67,5,16,0,0,66,65,1,0,0,0,66,67,1,0,0,0,67,7,1,0,0,0,68,73,
        5,25,0,0,69,70,5,15,0,0,70,72,5,25,0,0,71,69,1,0,0,0,72,75,1,0,0,
        0,73,71,1,0,0,0,73,74,1,0,0,0,74,9,1,0,0,0,75,73,1,0,0,0,76,77,5,
        2,0,0,77,81,5,19,0,0,78,80,3,12,6,0,79,78,1,0,0,0,80,83,1,0,0,0,
        81,79,1,0,0,0,81,82,1,0,0,0,82,84,1,0,0,0,83,81,1,0,0,0,84,85,5,
        20,0,0,85,11,1,0,0,0,86,88,3,14,7,0,87,89,5,16,0,0,88,87,1,0,0,0,
        88,89,1,0,0,0,89,95,1,0,0,0,90,92,3,16,8,0,91,93,5,16,0,0,92,91,
        1,0,0,0,92,93,1,0,0,0,93,95,1,0,0,0,94,86,1,0,0,0,94,90,1,0,0,0,
        95,13,1,0,0,0,96,97,5,6,0,0,97,98,5,23,0,0,98,99,5,14,0,0,99,100,
        5,23,0,0,100,102,5,17,0,0,101,103,3,20,10,0,102,101,1,0,0,0,102,
        103,1,0,0,0,103,104,1,0,0,0,104,105,5,18,0,0,105,15,1,0,0,0,106,
        107,5,7,0,0,107,108,5,23,0,0,108,109,5,12,0,0,109,111,5,23,0,0,110,
        112,3,18,9,0,111,110,1,0,0,0,111,112,1,0,0,0,112,17,1,0,0,0,113,
        114,5,21,0,0,114,115,5,9,0,0,115,116,5,13,0,0,116,117,5,26,0,0,117,
        118,5,22,0,0,118,19,1,0,0,0,119,124,3,22,11,0,120,121,5,15,0,0,121,
        123,3,22,11,0,122,120,1,0,0,0,123,126,1,0,0,0,124,122,1,0,0,0,124,
        125,1,0,0,0,125,21,1,0,0,0,126,124,1,0,0,0,127,128,5,23,0,0,128,
        129,5,13,0,0,129,130,3,24,12,0,130,23,1,0,0,0,131,139,5,25,0,0,132,
        139,5,24,0,0,133,139,5,11,0,0,134,139,5,26,0,0,135,139,5,10,0,0,
        136,139,3,26,13,0,137,139,3,28,14,0,138,131,1,0,0,0,138,132,1,0,
        0,0,138,133,1,0,0,0,138,134,1,0,0,0,138,135,1,0,0,0,138,136,1,0,
        0,0,138,137,1,0,0,0,139,25,1,0,0,0,140,141,5,17,0,0,141,146,3,24,
        12,0,142,143,5,15,0,0,143,145,3,24,12,0,144,142,1,0,0,0,145,148,
        1,0,0,0,146,144,1,0,0,0,146,147,1,0,0,0,147,149,1,0,0,0,148,146,
        1,0,0,0,149,150,5,18,0,0,150,27,1,0,0,0,151,152,5,21,0,0,152,157,
        3,24,12,0,153,154,5,15,0,0,154,156,3,24,12,0,155,153,1,0,0,0,156,
        159,1,0,0,0,157,155,1,0,0,0,157,158,1,0,0,0,158,160,1,0,0,0,159,
        157,1,0,0,0,160,161,5,22,0,0,161,29,1,0,0,0,162,163,5,3,0,0,163,
        167,5,19,0,0,164,166,3,32,16,0,165,164,1,0,0,0,166,169,1,0,0,0,167,
        165,1,0,0,0,167,168,1,0,0,0,168,170,1,0,0,0,169,167,1,0,0,0,170,
        171,5,20,0,0,171,31,1,0,0,0,172,173,5,23,0,0,173,174,5,13,0,0,174,
        176,3,24,12,0,175,177,5,16,0,0,176,175,1,0,0,0,176,177,1,0,0,0,177,
        33,1,0,0,0,17,37,42,61,66,73,81,88,92,94,102,111,124,138,146,157,
        167,176
    ]

class NNGraphParser ( Parser ):

    grammarFileName = "NNGraph.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'model'", "'graph'", "'config'", "'input'", 
                     "'output'", "'node'", "'edge'", "'tensor'", "'label'", 
                     "<INVALID>", "<INVALID>", "'->'", "'='", "':'", "','", 
                     "';'", "'('", "')'", "'{'", "'}'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "MODEL", "GRAPH", "CONFIG", "INPUT", 
                      "OUTPUT", "NODE", "EDGE", "TENSOR", "LABEL", "NONE", 
                      "BOOL", "ARROW", "ASSIGN", "COLON", "COMMA", "SEMI", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", 
                      "RBRACK", "ID", "FLOAT", "INT", "STRING", "LINE_COMMENT", 
                      "BLOCK_COMMENT", "WS" ]

    RULE_program = 0
    RULE_modelDecl = 1
    RULE_inputDecl = 2
    RULE_outputDecl = 3
    RULE_shape = 4
    RULE_graphDecl = 5
    RULE_graphStatement = 6
    RULE_nodeDecl = 7
    RULE_edgeDecl = 8
    RULE_edgeLabel = 9
    RULE_parameterList = 10
    RULE_parameter = 11
    RULE_value = 12
    RULE_tuple = 13
    RULE_list = 14
    RULE_configDecl = 15
    RULE_configEntry = 16

    ruleNames =  [ "program", "modelDecl", "inputDecl", "outputDecl", "shape", 
                   "graphDecl", "graphStatement", "nodeDecl", "edgeDecl", 
                   "edgeLabel", "parameterList", "parameter", "value", "tuple", 
                   "list", "configDecl", "configEntry" ]

    EOF = Token.EOF
    MODEL=1
    GRAPH=2
    CONFIG=3
    INPUT=4
    OUTPUT=5
    NODE=6
    EDGE=7
    TENSOR=8
    LABEL=9
    NONE=10
    BOOL=11
    ARROW=12
    ASSIGN=13
    COLON=14
    COMMA=15
    SEMI=16
    LPAREN=17
    RPAREN=18
    LBRACE=19
    RBRACE=20
    LBRACK=21
    RBRACK=22
    ID=23
    FLOAT=24
    INT=25
    STRING=26
    LINE_COMMENT=27
    BLOCK_COMMENT=28
    WS=29

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def modelDecl(self):
            return self.getTypedRuleContext(NNGraphParser.ModelDeclContext,0)


        def EOF(self):
            return self.getToken(NNGraphParser.EOF, 0)

        def graphDecl(self):
            return self.getTypedRuleContext(NNGraphParser.GraphDeclContext,0)


        def configDecl(self):
            return self.getTypedRuleContext(NNGraphParser.ConfigDeclContext,0)


        def getRuleIndex(self):
            return NNGraphParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = NNGraphParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.modelDecl()
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.state = 35
                self.graphDecl()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==3:
                    self.state = 36
                    self.configDecl()


                pass
            elif token in [3]:
                self.state = 39
                self.configDecl()
                self.state = 40
                self.graphDecl()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 44
            self.match(NNGraphParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModelDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MODEL(self):
            return self.getToken(NNGraphParser.MODEL, 0)

        def ID(self):
            return self.getToken(NNGraphParser.ID, 0)

        def LBRACE(self):
            return self.getToken(NNGraphParser.LBRACE, 0)

        def inputDecl(self):
            return self.getTypedRuleContext(NNGraphParser.InputDeclContext,0)


        def outputDecl(self):
            return self.getTypedRuleContext(NNGraphParser.OutputDeclContext,0)


        def RBRACE(self):
            return self.getToken(NNGraphParser.RBRACE, 0)

        def getRuleIndex(self):
            return NNGraphParser.RULE_modelDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModelDecl" ):
                listener.enterModelDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModelDecl" ):
                listener.exitModelDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModelDecl" ):
                return visitor.visitModelDecl(self)
            else:
                return visitor.visitChildren(self)




    def modelDecl(self):

        localctx = NNGraphParser.ModelDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_modelDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(NNGraphParser.MODEL)
            self.state = 47
            self.match(NNGraphParser.ID)
            self.state = 48
            self.match(NNGraphParser.LBRACE)
            self.state = 49
            self.inputDecl()
            self.state = 50
            self.outputDecl()
            self.state = 51
            self.match(NNGraphParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InputDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INPUT(self):
            return self.getToken(NNGraphParser.INPUT, 0)

        def ID(self):
            return self.getToken(NNGraphParser.ID, 0)

        def COLON(self):
            return self.getToken(NNGraphParser.COLON, 0)

        def TENSOR(self):
            return self.getToken(NNGraphParser.TENSOR, 0)

        def LPAREN(self):
            return self.getToken(NNGraphParser.LPAREN, 0)

        def shape(self):
            return self.getTypedRuleContext(NNGraphParser.ShapeContext,0)


        def RPAREN(self):
            return self.getToken(NNGraphParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(NNGraphParser.SEMI, 0)

        def getRuleIndex(self):
            return NNGraphParser.RULE_inputDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInputDecl" ):
                listener.enterInputDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInputDecl" ):
                listener.exitInputDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInputDecl" ):
                return visitor.visitInputDecl(self)
            else:
                return visitor.visitChildren(self)




    def inputDecl(self):

        localctx = NNGraphParser.InputDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_inputDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(NNGraphParser.INPUT)
            self.state = 54
            self.match(NNGraphParser.ID)
            self.state = 55
            self.match(NNGraphParser.COLON)
            self.state = 56
            self.match(NNGraphParser.TENSOR)
            self.state = 57
            self.match(NNGraphParser.LPAREN)
            self.state = 58
            self.shape()
            self.state = 59
            self.match(NNGraphParser.RPAREN)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 60
                self.match(NNGraphParser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OutputDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OUTPUT(self):
            return self.getToken(NNGraphParser.OUTPUT, 0)

        def ID(self):
            return self.getToken(NNGraphParser.ID, 0)

        def SEMI(self):
            return self.getToken(NNGraphParser.SEMI, 0)

        def getRuleIndex(self):
            return NNGraphParser.RULE_outputDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutputDecl" ):
                listener.enterOutputDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutputDecl" ):
                listener.exitOutputDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutputDecl" ):
                return visitor.visitOutputDecl(self)
            else:
                return visitor.visitChildren(self)




    def outputDecl(self):

        localctx = NNGraphParser.OutputDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_outputDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(NNGraphParser.OUTPUT)
            self.state = 64
            self.match(NNGraphParser.ID)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 65
                self.match(NNGraphParser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShapeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(NNGraphParser.INT)
            else:
                return self.getToken(NNGraphParser.INT, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(NNGraphParser.COMMA)
            else:
                return self.getToken(NNGraphParser.COMMA, i)

        def getRuleIndex(self):
            return NNGraphParser.RULE_shape

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShape" ):
                listener.enterShape(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShape" ):
                listener.exitShape(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShape" ):
                return visitor.visitShape(self)
            else:
                return visitor.visitChildren(self)




    def shape(self):

        localctx = NNGraphParser.ShapeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_shape)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(NNGraphParser.INT)
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 69
                self.match(NNGraphParser.COMMA)
                self.state = 70
                self.match(NNGraphParser.INT)
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GraphDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GRAPH(self):
            return self.getToken(NNGraphParser.GRAPH, 0)

        def LBRACE(self):
            return self.getToken(NNGraphParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(NNGraphParser.RBRACE, 0)

        def graphStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NNGraphParser.GraphStatementContext)
            else:
                return self.getTypedRuleContext(NNGraphParser.GraphStatementContext,i)


        def getRuleIndex(self):
            return NNGraphParser.RULE_graphDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGraphDecl" ):
                listener.enterGraphDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGraphDecl" ):
                listener.exitGraphDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGraphDecl" ):
                return visitor.visitGraphDecl(self)
            else:
                return visitor.visitChildren(self)




    def graphDecl(self):

        localctx = NNGraphParser.GraphDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_graphDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(NNGraphParser.GRAPH)
            self.state = 77
            self.match(NNGraphParser.LBRACE)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6 or _la==7:
                self.state = 78
                self.graphStatement()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
            self.match(NNGraphParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GraphStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nodeDecl(self):
            return self.getTypedRuleContext(NNGraphParser.NodeDeclContext,0)


        def SEMI(self):
            return self.getToken(NNGraphParser.SEMI, 0)

        def edgeDecl(self):
            return self.getTypedRuleContext(NNGraphParser.EdgeDeclContext,0)


        def getRuleIndex(self):
            return NNGraphParser.RULE_graphStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGraphStatement" ):
                listener.enterGraphStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGraphStatement" ):
                listener.exitGraphStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGraphStatement" ):
                return visitor.visitGraphStatement(self)
            else:
                return visitor.visitChildren(self)




    def graphStatement(self):

        localctx = NNGraphParser.GraphStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_graphStatement)
        self._la = 0 # Token type
        try:
            self.state = 94
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.nodeDecl()
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 87
                    self.match(NNGraphParser.SEMI)


                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.edgeDecl()
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 91
                    self.match(NNGraphParser.SEMI)


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NodeDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NODE(self):
            return self.getToken(NNGraphParser.NODE, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(NNGraphParser.ID)
            else:
                return self.getToken(NNGraphParser.ID, i)

        def COLON(self):
            return self.getToken(NNGraphParser.COLON, 0)

        def LPAREN(self):
            return self.getToken(NNGraphParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(NNGraphParser.RPAREN, 0)

        def parameterList(self):
            return self.getTypedRuleContext(NNGraphParser.ParameterListContext,0)


        def getRuleIndex(self):
            return NNGraphParser.RULE_nodeDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNodeDecl" ):
                listener.enterNodeDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNodeDecl" ):
                listener.exitNodeDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNodeDecl" ):
                return visitor.visitNodeDecl(self)
            else:
                return visitor.visitChildren(self)




    def nodeDecl(self):

        localctx = NNGraphParser.NodeDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_nodeDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(NNGraphParser.NODE)
            self.state = 97
            self.match(NNGraphParser.ID)
            self.state = 98
            self.match(NNGraphParser.COLON)
            self.state = 99
            self.match(NNGraphParser.ID)
            self.state = 100
            self.match(NNGraphParser.LPAREN)
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 101
                self.parameterList()


            self.state = 104
            self.match(NNGraphParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EdgeDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EDGE(self):
            return self.getToken(NNGraphParser.EDGE, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(NNGraphParser.ID)
            else:
                return self.getToken(NNGraphParser.ID, i)

        def ARROW(self):
            return self.getToken(NNGraphParser.ARROW, 0)

        def edgeLabel(self):
            return self.getTypedRuleContext(NNGraphParser.EdgeLabelContext,0)


        def getRuleIndex(self):
            return NNGraphParser.RULE_edgeDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEdgeDecl" ):
                listener.enterEdgeDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEdgeDecl" ):
                listener.exitEdgeDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEdgeDecl" ):
                return visitor.visitEdgeDecl(self)
            else:
                return visitor.visitChildren(self)




    def edgeDecl(self):

        localctx = NNGraphParser.EdgeDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_edgeDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(NNGraphParser.EDGE)
            self.state = 107
            self.match(NNGraphParser.ID)
            self.state = 108
            self.match(NNGraphParser.ARROW)
            self.state = 109
            self.match(NNGraphParser.ID)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 110
                self.edgeLabel()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EdgeLabelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(NNGraphParser.LBRACK, 0)

        def LABEL(self):
            return self.getToken(NNGraphParser.LABEL, 0)

        def ASSIGN(self):
            return self.getToken(NNGraphParser.ASSIGN, 0)

        def STRING(self):
            return self.getToken(NNGraphParser.STRING, 0)

        def RBRACK(self):
            return self.getToken(NNGraphParser.RBRACK, 0)

        def getRuleIndex(self):
            return NNGraphParser.RULE_edgeLabel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEdgeLabel" ):
                listener.enterEdgeLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEdgeLabel" ):
                listener.exitEdgeLabel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEdgeLabel" ):
                return visitor.visitEdgeLabel(self)
            else:
                return visitor.visitChildren(self)




    def edgeLabel(self):

        localctx = NNGraphParser.EdgeLabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_edgeLabel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(NNGraphParser.LBRACK)
            self.state = 114
            self.match(NNGraphParser.LABEL)
            self.state = 115
            self.match(NNGraphParser.ASSIGN)
            self.state = 116
            self.match(NNGraphParser.STRING)
            self.state = 117
            self.match(NNGraphParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NNGraphParser.ParameterContext)
            else:
                return self.getTypedRuleContext(NNGraphParser.ParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(NNGraphParser.COMMA)
            else:
                return self.getToken(NNGraphParser.COMMA, i)

        def getRuleIndex(self):
            return NNGraphParser.RULE_parameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterList" ):
                listener.enterParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterList" ):
                listener.exitParameterList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterList" ):
                return visitor.visitParameterList(self)
            else:
                return visitor.visitChildren(self)




    def parameterList(self):

        localctx = NNGraphParser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.parameter()
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 120
                self.match(NNGraphParser.COMMA)
                self.state = 121
                self.parameter()
                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(NNGraphParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(NNGraphParser.ASSIGN, 0)

        def value(self):
            return self.getTypedRuleContext(NNGraphParser.ValueContext,0)


        def getRuleIndex(self):
            return NNGraphParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = NNGraphParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(NNGraphParser.ID)
            self.state = 128
            self.match(NNGraphParser.ASSIGN)
            self.state = 129
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(NNGraphParser.INT, 0)

        def FLOAT(self):
            return self.getToken(NNGraphParser.FLOAT, 0)

        def BOOL(self):
            return self.getToken(NNGraphParser.BOOL, 0)

        def STRING(self):
            return self.getToken(NNGraphParser.STRING, 0)

        def NONE(self):
            return self.getToken(NNGraphParser.NONE, 0)

        def tuple_(self):
            return self.getTypedRuleContext(NNGraphParser.TupleContext,0)


        def list_(self):
            return self.getTypedRuleContext(NNGraphParser.ListContext,0)


        def getRuleIndex(self):
            return NNGraphParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = NNGraphParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_value)
        try:
            self.state = 138
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.match(NNGraphParser.INT)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.match(NNGraphParser.FLOAT)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 133
                self.match(NNGraphParser.BOOL)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 4)
                self.state = 134
                self.match(NNGraphParser.STRING)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 5)
                self.state = 135
                self.match(NNGraphParser.NONE)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 6)
                self.state = 136
                self.tuple_()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 7)
                self.state = 137
                self.list_()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TupleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(NNGraphParser.LPAREN, 0)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NNGraphParser.ValueContext)
            else:
                return self.getTypedRuleContext(NNGraphParser.ValueContext,i)


        def RPAREN(self):
            return self.getToken(NNGraphParser.RPAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(NNGraphParser.COMMA)
            else:
                return self.getToken(NNGraphParser.COMMA, i)

        def getRuleIndex(self):
            return NNGraphParser.RULE_tuple

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTuple" ):
                listener.enterTuple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTuple" ):
                listener.exitTuple(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTuple" ):
                return visitor.visitTuple(self)
            else:
                return visitor.visitChildren(self)




    def tuple_(self):

        localctx = NNGraphParser.TupleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_tuple)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(NNGraphParser.LPAREN)
            self.state = 141
            self.value()
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 142
                self.match(NNGraphParser.COMMA)
                self.state = 143
                self.value()
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 149
            self.match(NNGraphParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(NNGraphParser.LBRACK, 0)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NNGraphParser.ValueContext)
            else:
                return self.getTypedRuleContext(NNGraphParser.ValueContext,i)


        def RBRACK(self):
            return self.getToken(NNGraphParser.RBRACK, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(NNGraphParser.COMMA)
            else:
                return self.getToken(NNGraphParser.COMMA, i)

        def getRuleIndex(self):
            return NNGraphParser.RULE_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList" ):
                return visitor.visitList(self)
            else:
                return visitor.visitChildren(self)




    def list_(self):

        localctx = NNGraphParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(NNGraphParser.LBRACK)
            self.state = 152
            self.value()
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 153
                self.match(NNGraphParser.COMMA)
                self.state = 154
                self.value()
                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 160
            self.match(NNGraphParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConfigDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONFIG(self):
            return self.getToken(NNGraphParser.CONFIG, 0)

        def LBRACE(self):
            return self.getToken(NNGraphParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(NNGraphParser.RBRACE, 0)

        def configEntry(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NNGraphParser.ConfigEntryContext)
            else:
                return self.getTypedRuleContext(NNGraphParser.ConfigEntryContext,i)


        def getRuleIndex(self):
            return NNGraphParser.RULE_configDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConfigDecl" ):
                listener.enterConfigDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConfigDecl" ):
                listener.exitConfigDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConfigDecl" ):
                return visitor.visitConfigDecl(self)
            else:
                return visitor.visitChildren(self)




    def configDecl(self):

        localctx = NNGraphParser.ConfigDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_configDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(NNGraphParser.CONFIG)
            self.state = 163
            self.match(NNGraphParser.LBRACE)
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 164
                self.configEntry()
                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 170
            self.match(NNGraphParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConfigEntryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(NNGraphParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(NNGraphParser.ASSIGN, 0)

        def value(self):
            return self.getTypedRuleContext(NNGraphParser.ValueContext,0)


        def SEMI(self):
            return self.getToken(NNGraphParser.SEMI, 0)

        def getRuleIndex(self):
            return NNGraphParser.RULE_configEntry

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConfigEntry" ):
                listener.enterConfigEntry(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConfigEntry" ):
                listener.exitConfigEntry(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConfigEntry" ):
                return visitor.visitConfigEntry(self)
            else:
                return visitor.visitChildren(self)




    def configEntry(self):

        localctx = NNGraphParser.ConfigEntryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_configEntry)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(NNGraphParser.ID)
            self.state = 173
            self.match(NNGraphParser.ASSIGN)
            self.state = 174
            self.value()
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 175
                self.match(NNGraphParser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





