'''thonny-py5mode frontend
   interacts with py5mode backend (backend > py5_imported_mode_backend.py)
'''

import builtins
import jdk
import keyword
import os
import pathlib
import shutil
import site
import threading
import time
import types
from importlib import machinery, util
from thonny import editors, get_workbench, running, token_utils
from thonny import THONNY_USER_DIR
from thonny.languages import tr
from thonny.running import Runner
from tkinter.messagebox import showinfo

_PY5_IMPORTED_MODE = 'run.py5_imported_mode'
_REQUIRE_JDK = 17
_INSTALL_JDK_MESSAGE = '''
Thonny requires JDK to run py5 sketches. It\'ll need to download about 180 MB.

Click OK to proceed.
(it may seem like the window is stuck, but JDK is downloading)
'''


def set_java_home(jdk_path: pathlib.Path) -> None:
    '''add jdk path to config file (tools > options > general > env vars)'''
    jdk_path = 'JAVA_HOME=' + str(jdk_path)
    env_vars = get_workbench().get_option('general.environment')

    if jdk_path not in env_vars:
        env_vars.append(jdk_path)

    get_workbench().set_option('general.environment', env_vars)


def install_jdk() -> str:
    '''download and setup jdk (installs to thonny config directory)'''
    jdk_dir = 'jdk-' + str(_REQUIRE_JDK)

    system_jdk = 'TBD'
    # check system for existing jdk install (and if found, the version number)
    if os.environ.get('JAVA_HOME') is not None:
        system_jdk = os.environ['JAVA_HOME'].split('jdk-')[-1].split('.')[0]

    for name in os.listdir(THONNY_USER_DIR):
        # check for jdk in thonny config directory
        if name.startswith(jdk_dir):
            # set jdk path to thonny config directory
            set_java_home(pathlib.Path(THONNY_USER_DIR) / jdk_dir)
            return 'JAVA_HOME set'

    if not system_jdk.isdigit() or int(system_jdk) < _REQUIRE_JDK:
        print('> py5 requires jdk-%d' % _REQUIRE_JDK)
        showinfo('JDK for py5', _INSTALL_JDK_MESSAGE, master=get_workbench())

        for name in os.listdir(THONNY_USER_DIR):
            # delete existing thonny-py5mode jdk (if one exists)
            if name.startswith(jdk_dir):
                shutil.rmtree(pathlib.Path(install_to) / name)

        def display_progress(task: str) -> None:
            '''progress indicator for downloading jdk'''
            print(task)
            progress = '·'
            while not progress_complete:
                print(task + progress)
                progress += '·'
                time.sleep(1)

        # download jdk
        progress_complete = False
        dl_thread = threading.Thread(
          target=display_progress,
          args=('> downloading jdk ',)
        )
        dl_thread.start()
        jdk_file = jdk._download(jdk.get_download_url(_REQUIRE_JDK))
        progress_complete = True

        # extract jdk
        print('> extracting jdk')
        jdk._USER_DIR = THONNY_USER_DIR
        jdk_ext = jdk._get_normalized_compressed_file_ext(jdk_file)
        jdk._decompress_archive(jdk_file, jdk_ext, THONNY_USER_DIR)

        for name in os.listdir(THONNY_USER_DIR):
            # rename extracted jdk directory to jdk-11
            if name.startswith(jdk_dir):
                src = pathlib.Path(THONNY_USER_DIR) / name
                dest = pathlib.Path(THONNY_USER_DIR) / jdk_dir
                os.rename(src, dest)
                print('> done!')
                showinfo('', 'All done! py5 is ready.', master=get_workbench())
                break

        set_java_home(pathlib.Path(THONNY_USER_DIR) / dest)
        # one-off env var so there is no need to restart thonny on jdk install
        os.environ['JAVA_HOME'] = str(pathlib.Path(THONNY_USER_DIR) / dest)

        return 'JDK-11 installed and JAVA_HOME set'

    # set jdk path to thonny config directory
    set_java_home(pathlib.Path(THONNY_USER_DIR) / jdk_dir)
    return 'JAVA_HOME set'


def apply_recommended_py5_config() -> None:
    '''apply some recommended settings for thonny py5 work'''
    get_workbench().set_option('view.ui_theme', 'Kyanite UI')
    get_workbench().set_option('view.syntax_theme', 'Kyanite Syntax')
    get_workbench().set_option('assistance.open_assistant_on_errors', 'False')
    get_workbench().set_option('view.assistantview', False)
    get_workbench().hide_view('AssistantView')
    get_workbench().reload_themes()


def execute_imported_mode() -> None:
    '''run imported mode script using py5_tools run_sketch'''
    current_editor = get_workbench().get_editor_notebook().get_current_editor()
    current_file = current_editor.get_filename()

    if current_file is None:
        # thonny must 'save as' any new files, before it can run them
        editors.Editor.save_file(current_editor)
        current_file = current_editor.get_filename()

    if current_file and current_file.split('.')[-1] in ('py', 'py5', 'pyde'):
        # save and run py5 imported mode
        current_editor.save_file()
        run_sketch = '/py5_tools/tools/run_sketch.py'
        user_packages = str(site.getusersitepackages())
        site_packages = str(site.getsitepackages()[0])
        # check for py5 run_sketch path
        if pathlib.Path(user_packages + run_sketch).is_file():
            run_sketch = pathlib.Path(user_packages + run_sketch)
        elif pathlib.Path(site_packages + run_sketch).is_file():
            run_sketch = pathlib.Path(site_packages + run_sketch)
        else:
            run_sketch = pathlib.Path(get_python_lib() + run_sketch)

        working_directory = os.path.dirname(current_file)
        cd_cmd_line = running.construct_cd_command(working_directory) + '\n'
        cmd_parts = ['%Run', str(run_sketch), current_file]
        ed_token = [running.EDITOR_CONTENT_TOKEN]
        exe_cmd_line = running.construct_cmd_line(cmd_parts, ed_token) + '\n'
        running.get_shell().submit_magic_command(cd_cmd_line + exe_cmd_line)


def patched_execute_current(self: Runner, command_name: str) -> None:
    '''override run button behavior for py5 imported mode'''
    execute_imported_mode()


def patch_token_coloring() -> None:
    '''add py5 keywords to syntax highlighting'''
    spec = util.find_spec('py5_tools')
    # cannot use `dir(py5)` because of jvm check, hence direct loading
    path = pathlib.Path(spec.submodule_search_locations[0]) / 'reference.py'
    loader = machinery.SourceFileLoader('py5_tools_reference', str(path))
    module = types.ModuleType(loader.name)
    loader.exec_module(module)
    # add keywords to thonny builtin list
    patched_builtinlist = token_utils._builtinlist + module.PY5_ALL_STR
    matches = token_utils.matches_any('builtin', patched_builtinlist)
    patched_BUILTIN = r'([^.\'"\\#]\b|^)' + (matches + r'\b')
    token_utils.BUILTIN = patched_BUILTIN


def set_py5_imported_mode() -> None:
    '''set imported mode variable in thonny configuration.ini file'''
    if get_workbench().in_simple_mode():
        os.environ['PY5_IMPORTED_MODE'] = 'auto'
    else:
        p_i_m = str(get_workbench().get_option(_PY5_IMPORTED_MODE))
        os.environ['PY5_IMPORTED_MODE'] = p_i_m

        # switch on/off py5 run button behavior
        if get_workbench().get_option(_PY5_IMPORTED_MODE):
            Runner._original_execute_current = Runner.execute_current
            Runner.execute_current = patched_execute_current
        else:
            try:
                Runner.execute_current = Runner._original_execute_current
            except:
                pass


def toggle_py5_imported_mode() -> None:
    '''toggle py5 imported mode settings'''
    var = get_workbench().get_variable(_PY5_IMPORTED_MODE)
    var.set(not var.get())
    install_jdk()
    set_py5_imported_mode()


def load_plugin() -> None:
    get_workbench().set_default(_PY5_IMPORTED_MODE, False)
    get_workbench().add_command(
      'toggle_py5_imported_mode',
      'py5',
      tr('Imported mode for py5'),
      toggle_py5_imported_mode,
      flag_name=_PY5_IMPORTED_MODE,
      group=10,
    )
    get_workbench().add_command(
      'apply_recommended_py5_config',
      'py5',
      tr('Apply recommended py5 settings'),
      apply_recommended_py5_config,
      group=20,
    )
    patch_token_coloring()
    set_py5_imported_mode()
