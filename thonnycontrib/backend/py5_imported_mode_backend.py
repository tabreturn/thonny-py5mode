import ast
import os
import sys

from thonny.plugins.cpython.cpython_backend import get_backend, MainCPythonBackend
from py5_tools import *


def augment_ast(root):
    mode = os.environ.get('PY5_IMPORTED_MODE', 'False')
    assert mode != 'False'
    try:
        import py5  # @UnusedImport
        print('PY5 FOUND.................................')
    except ImportError:
        if mode == 'True':
            print('PY5 NOT FOUND.........................')
        return

    imported.run_code('/home/nuc/Desktop/a.py')


def patched_editor_autocomplete(self, cmd):
    # Make extra builtins visible for Jedi
    prefix = "from py5 import *\n"
    cmd["source"] = prefix + cmd["source"]
    cmd["row"] = cmd["row"] + 1
    print('AUTOCOMPLETING................................')
    result = get_backend()._original_editor_autocomplete(cmd)
    result["row"] = result["row"] - 1
    result["source"] = result["source"][len(prefix) :]

    return result


def load_plugin():
    if os.environ.get("PY5_IMPORTED_MODE", "False").lower() == "false":
        return
    print('LOAD PY5 BACKEND .............................')
    get_backend().add_ast_postprocessor(augment_ast)
    MainCPythonBackend._original_editor_autocomplete = MainCPythonBackend._cmd_editor_autocomplete
    MainCPythonBackend._cmd_editor_autocomplete = patched_editor_autocomplete
