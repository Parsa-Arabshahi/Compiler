from antlr4 import *

from generated.NNGraphLexer import NNGraphLexer
from generated.NNGraphParser import NNGraphParser

from ast_builder import ASTBuilder
from semantic import SemanticAnalyzer
from codegen import CodeGenerator
from graphviz_exporter import GraphvizExporter
#from shape_inference import ShapeInference

import sys


def compile_file(input_file, output_file):

    stream = FileStream(input_file, encoding="utf-8")

    lexer = NNGraphLexer(stream)

    tokens = CommonTokenStream(lexer)

    parser = NNGraphParser(tokens)

    tree = parser.program()

    ast = ASTBuilder().visit(tree)
    print("Nodes:")
    for n in ast.nodes:
        print(n.id, n.layer_type)

    print("\nEdges:")
    for e in ast.edges:
        print(e.source, "->", e.target)

    # ast = ShapeInference(ast).infer()
    # for node in ast.nodes:
    #     print(node.id, node.params)
    SemanticAnalyzer(ast).analyze()

    code = CodeGenerator(ast).generate()

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(code)

    dot = GraphvizExporter(ast).export()

    with open("model.dot", "w") as f:
        f.write(dot)

    print("Compilation successful.")

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: python nngraph_compiler.py input.nng output.py")
        sys.exit(1)

    compile_file(sys.argv[1], sys.argv[2])
    