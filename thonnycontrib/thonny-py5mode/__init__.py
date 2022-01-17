'''thonny-py5mode frontend
   interacts with thonny-py5mode backend (backend > py5_imported_mode_backend.py)
'''

import os
import jdk
import pathlib
import shutil
import threading
import time
from thonny import get_workbench, THONNY_USER_DIR
from thonny.languages import tr
from tkinter.messagebox import showinfo

_PY5_IMPORTED_MODE = 'run.py5_imported_mode'
_REQUIRE_JDK = 11
_INSTALL_JDK_MESSAGE = '''
Thonny requires JDK to run py5 sketches. It\'ll need to download about 180 MB.
Click OK to proceed
(it may seem like this window is stuck, but JDK is downloading)
'''


def set_java_home(jdk_path: pathlib.Path) -> None:
    '''add jdk path to config file (tools > options > general > env vars)'''
    jdk_path = 'JAVA_HOME=' + str(jdk_path)
    env_vars = get_workbench().get_option('general.environment')

    if jdk_path not in env_vars:
        env_vars.append(jdk_path)

    get_workbench().set_option('general.environment', env_vars)


def install_jdk() -> None:
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
          target = display_progress,
          args = ('> downloading jdk ',)
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
        return 'JDK-11 installed and JAVA_HOME set'

    # set jdk path to thonny config directory
    set_java_home(pathlib.Path(THONNY_USER_DIR) / jdk_dir)
    return 'JAVA_HOME set'


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
    install_jdk()
    set_py5_imported_mode()


def apply_recommended_py5_config() -> None:  # ADD A RESTORE (TO EARLIER SETTINGS) FEATURE <---
    '''apply some recommended settings for thonny py5 work'''
    get_workbench().set_option('view.ui_theme', 'Kyanite UI')
    get_workbench().set_option('view.syntax_theme', 'Kyanite Syntax')
    get_workbench().set_option('assistance.open_assistant_on_errors', 'False')
    get_workbench().reload_themes()


def load_plugin() -> None:
    get_workbench().set_default(_PY5_IMPORTED_MODE, False)
    get_workbench().add_command(
      'toggle_py5_imported_mode',
      'py5',
      tr('Imported mode for py5'),
      activate_py5_imported_mode,
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
    set_py5_imported_mode()
