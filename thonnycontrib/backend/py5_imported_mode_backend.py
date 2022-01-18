'''thonny-py5mode backend
   interacts with thonny-py5mode frontend (thonny-py5mode > __init__.py)
'''

import ast
import os
import sys

from py5_tools import imported
from thonny.common import InlineCommand, InlineResponse
from thonny.plugins.cpython.cpython_backend import (
  get_backend,
  MainCPythonBackend
)


def patched_editor_autocomplete(
      self: MainCPythonBackend, cmd: InlineCommand) -> InlineResponse:
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

    # note that _cmd_editor_autocomplete is not a public api
    # may need to treat different thonny versions differently
    # https://groups.google.com/g/thonny/c/wWCeXWpKy8c/m/tXDdQCs6AgAJ
    c_e_a = MainCPythonBackend._cmd_editor_autocomplete
    MainCPythonBackend._original_editor_autocomplete = c_e_a
    MainCPythonBackend._cmd_editor_autocomplete = patched_editor_autocomplete
