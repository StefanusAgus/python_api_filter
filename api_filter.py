import ast
import _ast
from ast import *
import sys
import os

class ApiLocator(ast.NodeVisitor):
    function_name = ""

    def __init__(self, fname):
        self.function_name = fname
        super().__init__()

    # helper function to get the API invocation or function name from the node
    # e.g.
    # getFunctionName("sklearn.dummy.DummyClassifier") should return "DummyClassifier"
    # getFunctionName("DummyClassifier") should also return "Dummy Classifier"
    def getFunctionName(self, node):
        try:
            return node.func.id
        except:
            return node.func.attr

    def getScopeNode(self, node):
        try:
            return node.func.value
        except:
            return None

    def recurseScope(self, node):
        scope = self.getScopeNode(node)
        if scope is not None:
            # Has scope that might be function call too
            if isinstance(scope, _ast.Call):
                node_function_name = self.getFunctionName(scope)
                if node_function_name == self.function_name:
                    print("Found API invocation in line: " + node.lineno.__str__())
            self.recurseScope(scope)


    def visit_Call(self, node: Call):
        node_function_name = self.getFunctionName(node)
        self.recurseScope(node)
        if node_function_name == self.function_name:
            print("Found API invocation in line: " + node.lineno.__str__())

def sanitize_function(str):
    return_str = str.strip()
    return_str = ''.join(e for e in return_str if e.isalnum())
    return return_str


if len(sys.argv) < 3:
    print("USAGE: ")
    print('python api_filter.py "PATH_TO_FILE" "FUNCTION_NAME"')
    print('e.g. : python.api.filter.py "../testfile.py" "kmeans"')
    print('FUNCTION_NAME is case-sensitive')
    exit()

path_to_file = sys.argv[1]
function_name = sanitize_function(sys.argv[2])
if not os.path.isfile(path_to_file):
    print("File does not exist, quitting...")
    exit()

print("\nSearching for: '" + function_name + "' API invocation in:")
print(path_to_file + " file...\n")

with open(path_to_file, "r") as source:
    tree = ast.parse(source.read())
    defaultValueChange = ApiLocator(function_name)
    defaultValueChange.visit(tree)
