import os

from thonny import get_workbench
from thonny.languages import tr

_OPTION_NAME = 'run.py5_imported_mode'


def toggle_variable():
    var = get_workbench().get_variable(_OPTION_NAME)
    var.set(not var.get())
    update_environment()


def set_jdk_path():
    # THIS SHOULD HAPPEN WHEN JDK IS INSTALLED
    # MAKE JDK PATH DYNAMIC --
    jdk_path = 'JAVA_HOME=/home/nuc/.config/Thonny/jdk-11/'
    env_vars = get_workbench().get_option('general.environment')
    if jdk_path not in env_vars:
        env_vars.append(jdk_path)


def py5_config() -> None:
    set_jdk_path()
    # ADDITIONAL RECOMMENDED SETTINGS
    get_workbench().set_option('view.ui_theme', 'Kyanite UI')
    get_workbench().set_option('view.syntax_theme', 'Kyanite Syntax')
    get_workbench().set_option('assistance.open_assistant_on_errors', 'False')
    get_workbench().reload_themes()
    update_environment()


def update_environment():
    if get_workbench().in_simple_mode():
        os.environ['PY5_IMPORTED_MODE'] = 'auto'
    else:
        os.environ['PY5_IMPORTED_MODE'] = str(get_workbench().get_option(_OPTION_NAME))


def load_plugin() -> None:
    get_workbench().set_default(_OPTION_NAME, False)
    get_workbench().add_command(
        'toggle_py5_imported_mode',
        'py5',
        tr('py5 imported mode'),
        toggle_variable,
        flag_name=_OPTION_NAME,
        group=10,
    )
    get_workbench().add_command(
        'toggle_py5_config',
        'py5',
        tr('py5 config'),
        py5_config,
        group=10,
    )
    update_environment()
