grammar NNGraph;

//====================
// Parser
//====================

program
    : modelDecl (graphDecl configDecl? | configDecl graphDecl) EOF
    ;

modelDecl
    : MODEL ID LBRACE
        inputDecl
        outputDecl
      RBRACE
    ;

inputDecl
    : INPUT ID COLON TENSOR LPAREN shape RPAREN SEMI?
    ;

outputDecl
    : OUTPUT ID SEMI?
    ;

shape
    : INT (COMMA INT)*
    ;

graphDecl
    : GRAPH LBRACE
        graphStatement*
      RBRACE
    ;

graphStatement
    : nodeDecl SEMI?
    | edgeDecl SEMI?
    ;

nodeDecl
    : NODE ID COLON ID LPAREN parameterList? RPAREN
    ;

edgeDecl
    : EDGE ID ARROW ID edgeLabel?
    ;

edgeLabel
    : LBRACK LABEL ASSIGN STRING RBRACK
    ;

parameterList
    : parameter (COMMA parameter)*
    ;

parameter
    : ID ASSIGN value
    ;

value
    : INT
    | FLOAT
    | BOOL
    | STRING
    | NONE
    | tuple
    | list
    ;

tuple
    : LPAREN value (COMMA value)* RPAREN
    ;

list
    : LBRACK value (COMMA value)* RBRACK
    ;

configDecl
    : CONFIG LBRACE
        configEntry*
      RBRACE
    ;

configEntry
    : ID ASSIGN value SEMI?
    ;

//====================
// Lexer
//====================

MODEL      : 'model';
GRAPH      : 'graph';
CONFIG     : 'config';

INPUT      : 'input';
OUTPUT     : 'output';

NODE       : 'node';
EDGE       : 'edge';

TENSOR     : 'tensor';

LABEL      : 'label';

NONE
    : 'None'
    | 'null'
    ;

BOOL
    : 'true'
    | 'false'
    | 'True'
    | 'False'
    ;

ARROW      : '->';

ASSIGN     : '=';

COLON       : ':';
COMMA       : ',';
SEMI        : ';';

LPAREN      : '(';
RPAREN      : ')';

LBRACE      : '{';
RBRACE      : '}';

LBRACK      : '[';
RBRACK      : ']';

ID
    : [a-zA-Z_][a-zA-Z0-9_]*
    ;

FLOAT
    : '-'? [0-9]+ '.' [0-9]+
    ;

INT
    : '-'? [0-9]+
    ;

STRING
    : '"' (~["\\] | '\\' .)* '"'
    ;

LINE_COMMENT
    : '//' ~[\r\n]* -> skip
    ;

BLOCK_COMMENT
    : '/*' .*? '*/' -> skip
    ;

WS
    : [ \t\r\n]+ -> skip
    ;