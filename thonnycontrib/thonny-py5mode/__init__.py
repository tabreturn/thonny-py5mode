'''thonny-py5mode frontend
   interacts with thonny-py5mode backend (backend > py5_imported_mode_backend.py)
'''

import os

from thonny import get_workbench
from thonny.languages import tr

_PY5_IMPORTED_MODE = 'run.py5_imported_mode'


def set_py5_imported_mode() -> None:
    '''set variable to switch on/off py5 run button behavior'''
    if get_workbench().in_simple_mode():
        os.environ['PY5_IMPORTED_MODE'] = 'auto'
    else:
        p_i_m = str(get_workbench().get_option(_PY5_IMPORTED_MODE))
        os.environ['PY5_IMPORTED_MODE'] = p_i_m


def activate_py5_imported_mode() -> None:
    '''activate py5 imported mode settings'''
    var = get_workbench().get_variable(_PY5_IMPORTED_MODE)
    # toggle variable (and menu checkbox)
    var.set(not var.get())
    set_py5_imported_mode()


def set_jdk_path() -> None:  # CALL THIS WHEN JDK IS INSTALLED <---
    '''add jdk path to config file (tools > options > general > env vars)'''
    jdk_path = 'JAVA_HOME=/home/nuc/.config/Thonny/jdk-11/'  # MAKE JDK PATH DYNAMIC <---
    env_vars = get_workbench().get_option('general.environment')

    if jdk_path not in env_vars:
        env_vars.append(jdk_path)

    get_workbench().set_option('general.environment', env_vars)


def apply_recommended_py5_config() -> None:  # ADD A RESTORE (TO EARLIER SETTINGS) FEATURE <---
    '''apply some recommended settings for thonny py5 work'''
    set_jdk_path()
    get_workbench().set_option('view.ui_theme', 'Kyanite UI')
    get_workbench().set_option('view.syntax_theme', 'Kyanite Syntax')
    get_workbench().set_option('assistance.open_assistant_on_errors', 'False')
    get_workbench().reload_themes()


def load_plugin() -> None:
    get_workbench().set_default(_PY5_IMPORTED_MODE, False)
    get_workbench().add_command(
      'toggle_py5_imported_mode',
      'py5',
      tr('py5 imported mode'),
      activate_py5_imported_mode,
      flag_name=_PY5_IMPORTED_MODE,
      group=10,
    )
    get_workbench().add_command(
      'apply_recommended_py5_config',
      'py5',
      tr('apply recommended py5 settings'),
      apply_recommended_py5_config,
      group=20,
    )
    set_py5_imported_mode()
