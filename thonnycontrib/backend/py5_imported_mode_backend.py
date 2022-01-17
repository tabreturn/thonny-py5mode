'''thonny-py5mode backend
   interacts with thonny-py5mode frontend (thonny-py5mode > __init__.py)
'''

import ast
import os
import sys

from py5_tools import imported
from thonny.common import InlineResponse
from thonny.plugins.cpython.cpython_backend import (
  get_backend,
  MainCPythonBackend
)


def augment_ast(root) -> None:
    '''augment run button for thonny imported mode'''
    mode = os.environ.get('PY5_IMPORTED_MODE', 'False')
    assert mode != 'False'

    # check for py5 package
    try:
        import py5  # @UnusedImport
    except ImportError:
        if mode == 'True':
            print('py5 package not found')
        return

    # execute script
    current_file = os.path.join(sys.path[0], sys.argv[0])
    imported.run_code(current_file)


def patched_editor_autocomplete(self, cmd) -> InlineResponse:
    '''add py5 to autocompletion'''
    prefix = 'from py5 import *\n'
    cmd['source'] = prefix + cmd['source']
    cmd['row'] = cmd['row'] + 1
    result = get_backend()._original_editor_autocomplete(cmd)
    result['row'] = result['row'] - 1
    result['source'] = result['source'][len(prefix):]
    return result


def load_plugin() -> None:
    '''every thonny plug-in uses this function to load'''
    if os.environ.get('PY5_IMPORTED_MODE', 'False').lower() == 'false':
        return

    get_backend().add_ast_postprocessor(augment_ast)
    c_e_a = MainCPythonBackend._cmd_editor_autocomplete
    MainCPythonBackend._original_editor_autocomplete = c_e_a
    MainCPythonBackend._cmd_editor_autocomplete = patched_editor_autocomplete
