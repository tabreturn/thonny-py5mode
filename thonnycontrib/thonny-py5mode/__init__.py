import os

from thonny import get_workbench
from thonny.languages import tr

_PY5_IMPORTED_MODE = 'run.py5_imported_mode'


def update_environment() -> None:
    '''set mode in configuration.ini file'''
    if get_workbench().in_simple_mode():
        os.environ['PY5_IMPORTED_MODE'] = 'auto'
    else:
        pim = str(get_workbench().get_option(_PY5_IMPORTED_MODE))
        os.environ['PY5_IMPORTED_MODE'] = pim


def toggle_variable() -> None:
    '''toggle variables'''
    var = get_workbench().get_variable(_PY5_IMPORTED_MODE)
    var.set(not var.get())
    update_environment()


def set_jdk_path() -> None:  # CALL THIS WHEN JDK IS INSTALLED <---
    '''add jdk path to config file (tools > options > general > env vars)'''
    jdk_path = 'JAVA_HOME=/home/nuc/.config/Thonny/jdk-11/'  # MAKE JDK PATH DYNAMIC <---
    env_vars = get_workbench().get_option('general.environment')

    if jdk_path not in env_vars:
        env_vars.append(jdk_path)


def apply_recommended_py5_config() -> None:  # ADD A RESTORE (TO EARLIER SETTINGS) FEATURE <---
    '''apply some recommended settings for thonny py5 work'''
    set_jdk_path()
    get_workbench().set_option('view.ui_theme', 'Kyanite UI')
    get_workbench().set_option('view.syntax_theme', 'Kyanite Syntax')
    get_workbench().set_option('assistance.open_assistant_on_errors', 'False')
    get_workbench().reload_themes()
    update_environment()


def load_plugin() -> None:
    get_workbench().set_default(_PY5_IMPORTED_MODE, False)
    get_workbench().add_command(
        'toggle_py5_imported_mode',
        'py5',
        tr('py5 imported mode'),
        toggle_variable,
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
    update_environment()
