'''
thonny-py5mode.

py5 plugin for Thonny.

# NOTES TO SELF:
* documentation: https://github.com/thonny/thonny/wiki/Plugins
* maybe look at how Run > Pygame Zero Mode is programmed?
'''

import os
import pathlib
import shutil
import subprocess
import site
import sys
import threading
import time
from tkinter.messagebox import showinfo
import jdk
from py5_tools import imported
from thonny.languages import tr
from thonny import get_workbench, THONNY_USER_DIR
from thonny import running
from thonny.ui_utils import select_sequence

__author__ = 'tabreturn'
__credits__ = 'organisation name'


def set_java_home(jdk_path: str) -> None:
    '''set jdk path to thonny/lib/jdk-11'''
    os.environ['JAVA_HOME'] = str(jdk_path)


REQUIRE_JDK = 11


def activate_py5(install_type: str):
    '''get thonny (portable version) paths'''
    jdk_dir = 'jdk-' + str(REQUIRE_JDK)
    system_jdk = 'TBD'
    # check system for jdk install (and version, if found)
    if os.environ.get('JAVA_HOME') is not None:
        system_jdk = os.environ['JAVA_HOME'].split('jdk-')[-1].split('.')[0]
    # install to app directory if portable, config directory if non-portable
    thonny_exec = os.path.dirname(sys.executable)
    install_to = thonny_exec if install_type == 'portable' else THONNY_USER_DIR

    for name in os.listdir(install_to):
        # check for jdk directory thonny app / config directory
        if name.startswith(jdk_dir):
            # set jdk path to thonny app / config directory
            set_java_home(pathlib.Path(install_to) / jdk_dir)
            return 'JAVA_HOME set'

    if not system_jdk.isdigit() or int(system_jdk) < REQUIRE_JDK:
        print('> py5 requires jdk-%d' % REQUIRE_JDK)
        install_msg = '''
Thonny requires JDK to run py5 sketches. It\'ll need to download about 180 MB.

Click OK to proceed
(it may seem like this window is stuck, but JDK is downloading)
'''
        showinfo('JDK for py5', install_msg, master=get_workbench())

        for name in os.listdir(install_to):
            # delete existing *thonny-py5mode jdk*
            if name.startswith(jdk_dir):
                shutil.rmtree(pathlib.Path(install_to) / name)

        def display_progress(task: str):
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
        jdk_file = jdk._download(jdk.get_download_url(REQUIRE_JDK))
        progress_complete = True

        # extract jdk
        print('> extracting jdk')
        jdk._USER_DIR = install_to
        jdk_ext = jdk._get_normalized_compressed_file_ext(jdk_file)
        jdk._decompress_archive(jdk_file, jdk_ext, install_to)

        for name in os.listdir(install_to):
            # rename extracted jdk directory to jdk-11
            if name.startswith(jdk_dir):
                src = pathlib.Path(install_to) / name
                dest = pathlib.Path(install_to) / jdk_dir
                os.rename(src, dest)
                print('> done!')
                showinfo('', 'All done! py5 is ready.', master=get_workbench())
                break

        set_java_home(pathlib.Path(install_to) / dest)
        return 'JDK-11 installed and JAVA_HOME set'

    # set jdk path to thonny app / config directory
    set_java_home(pathlib.Path(install_to) / jdk_dir)
    return 'JAVA_HOME set'


def execute_module_mode() -> None:
    '''
    there's got to be a better approach than this ...
    maybe something that employs a new Runner instance
    maybe something that changes the thonny's default run behaviour
    '''
    current_editor = get_workbench().get_editor_notebook().get_current_editor()
    current_file = current_editor.get_filename()

    if current_file is None:
        # thonny must 'save as' any new files, before it can run them
        showinfo(
          'py5 module mode error',
          'Save your file somewhere first',
          master=get_workbench()
        )

    elif current_file and current_file.split('.')[-1] in ('py', 'py5', 'pyde'):
        # save and run py5 module mode
        current_editor.save_file()
        run_sketch = '/py5_tools/tools/run_sketch.py'
        user_packages = str(site.getusersitepackages())
        site_packages = str(site.getsitepackages()[0])
        # check for py5 run_sketch path
        if pathlib.Path(user_packages + run_sketch).is_file():
            run_sketch = pathlib.Path(user_packages + run_sketch)
        elif pathlib.Path(site_packages + run_sketch).is_file():
            run_sketch = pathlib.Path(site_packages + run_sketch)

        working_directory = os.path.dirname(current_file)
        cd_cmd_line = running.construct_cd_command(working_directory) + '\n'
        cmd_parts = ['%Run', str(run_sketch), current_file]
        ed_token = [running.EDITOR_CONTENT_TOKEN]
        exe_cmd_line = running.construct_cmd_line(cmd_parts, ed_token) + '\n'
        running.get_shell().submit_magic_command(cd_cmd_line + exe_cmd_line)


# workaround for .add_command() handler parameter that won't accept arguments
def toggle_variable_portable() -> None: toggle_variable('portable')
def toggle_variable_installed() -> None: toggle_variable('installed')


def toggle_variable(install_type: str) -> None:
    '''install_type is portable or installed'''
    var_portable = get_workbench().get_variable('run.py5_mode_portable')
    var_installed = get_workbench().get_variable('run.py5_mode_installed')

    if install_type == 'portable':
        var_installed.set(False)
        var_portable.set(not var_portable.get())

    if install_type == 'installed':
        var_portable.set(False)
        var_installed.set(not var_installed.get())

    # NOTE: don't know what this is for
    # if get_workbench().in_simple_mode():
    #     os.environ['PY5_MODE'] = 'auto'
    # else:
    #     os.environ['PY5_MODE'] = str(get_workbench().get_option(_OPTION_...))

    if var_portable.get() or var_installed.get():
        # activate py5 (and download jdk if necessary)
        activate_py5(install_type)


def load_plugin() -> None:
    '''every thonny plug-in uses this function to load'''
    # portable button
    get_workbench().set_option('run.py5_mode_portable', False)
    '''
    FIX: jdk installs to wherever thonny is run *from* (not relatice to exec)
    get_workbench().add_command(
      'toggle_py5_mode_portable',
      'py5',
      tr('py5 mode for portable Thonny'),
      toggle_variable_portable,
      flag_name='run.py5_mode_portable',
      group=100
    )
    '''
    # non-portable / installed button
    get_workbench().set_option('run.py5_mode_installed', False)
    get_workbench().add_command(
      'toggle_py5_mode_installed',
      'py5',
      tr('Activate py5 mode for Thonny'),#tr('py5 mode for installed Thonny'),
      toggle_variable_installed,
      flag_name='run.py5_mode_installed',
      group=100
    )
    # run link
    # NOTE: perhaps this should be a toggle that in-turn affects thonny run?
    get_workbench().add_command(
      'execute_module_mode',
      'py5',
      'Run imported mode sketch',
      execute_module_mode,
      default_sequence='<Control-u>',
      extra_sequences=[select_sequence('<Control-Alt-u>', '<Command-u>')],
      group=200
    )

