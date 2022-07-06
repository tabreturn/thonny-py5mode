'''thonny-py5mode jdk installer
   checks
'''

import jdk
import os
import pathlib
import threading
import time
from thonny import THONNY_USER_DIR, get_workbench
from tkinter.messagebox import showinfo


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


def install_jdk(require_jdk: int) -> str:
    '''download and setup jdk (installs to thonny config directory)'''
    jdk_dir = 'jdk-' + str(require_jdk)

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

    if not system_jdk.isdigit() or int(system_jdk) < require_jdk:
        print('> py5 requires jdk-%d' % require_jdk)
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
        jdk_file = jdk._download(jdk.get_download_url(require_jdk))
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

        return f'JDK-{require_jdk} installed and JAVA_HOME set'

    # set jdk path to thonny config directory
    set_java_home(pathlib.Path(THONNY_USER_DIR) / jdk_dir)
    return 'JAVA_HOME set'
