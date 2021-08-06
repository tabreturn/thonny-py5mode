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
import sys
# for jdk downloader (https://pypi.org/project/install-jdk/)
import threading
import time
import jdk
# thonny plugin imports
from thonny import get_workbench, THONNY_USER_DIR
from thonny.languages import tr
from tkinter.messagebox import showinfo

__author__ = 'tabreturn'
__credits__ = 'organisation name'


def set_java_home(jdk_path):
    '''set jdk path to thonny/lib/jdk-11'''
    os.environ['JAVA_HOME'] = str(jdk_path)


def activate_py5(install_type):
    '''get thonny (portable version) paths'''
    require_jdk = 11
    jdk_dir = 'jdk-' + str(require_jdk)
    no_jdk_dir = True
    system_jdk = os.environ['JAVA_HOME'].split('jdk-')[-1].split('.')[0]
    # install to app directory if portable, config directory if non-portable
    install_to = sys.path[0] if install_type == 'portable' else THONNY_USER_DIR

    for name in os.listdir(install_to):
        # check for jdk directory thonny app / config directory
        if name.startswith(jdk_dir):
            no_jdk_dir = False

    if no_jdk_dir or not system_jdk.isdigit() or int(system_jdk) < require_jdk:
        print('> py5 requires jdk-11')

        for name in os.listdir(install_to):
            # delete existing *thonny-py5mode jdk*
            if name.startswith(jdk_dir):
                shutil.rmtree(pathlib.Path(install_to) / name)

        def display_progress(task):
            '''progress indicator for downloading jdk'''
            print(task)
            progress = '·'
            while not progress_complete:
                print(task + progress)
                progress += '·'
                time.sleep(1)

        # download jdk
        progress_complete = False
        msg = '> downloading jdk '
        dl_thread = threading.Thread(target=display_progress, args=(msg,))
        dl_thread.start()
        jdk_file = jdk._download(jdk.get_download_url(require_jdk))
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
                break

        set_java_home(pathlib.Path(install_to) / dest)
        return 'JDK-11 installed and JAVA_HOME set'

    else:
        # set jdk path to thonny app / config directory
        set_java_home(pathlib.Path(install_to) / jdk_dir)
        return 'JAVA_HOME set'


_OPTION_PORTABLE = 'run.py5_mode_portable'
_OPTION_INSTALLED = 'run.py5_mode_installed'
# workaround for .add_command() handler parameter that won't accept arguments
def toggle_variable_portable(): toggle_variable('portable')
def toggle_variable_installed(): toggle_variable('installed')


def toggle_variable(install_type):
    '''install_type is portable or installed'''
    var_portable = get_workbench().get_variable(_OPTION_PORTABLE)
    var_installed = get_workbench().get_variable(_OPTION_INSTALLED)

    if install_type == 'portable':
        var_installed.set(False)
        var_portable.set(not var_portable.get())

    if install_type == 'installed':
        var_portable.set(False)
        var_installed.set(not var_installed.get())

    '''DON'T KNOW WHAT THIS IS FOR
    if get_workbench().in_simple_mode():
        os.environ['PY5_MODE'] = 'auto'
    else:
        os.environ['PY5_MODE'] = str(get_workbench().get_option(_OPTION_...))
    '''
    if var_portable.get() or var_installed.get():
        # activate py5 (and download jdk if necessary)
        showinfo(activate_py5(install_type), 'py5 mode activated')


def load_plugin():
    '''every thonny plug-in uses this function to load'''
    # portable button
    get_workbench().set_default(_OPTION_PORTABLE, False)
    get_workbench().add_command(
        'toggle_py5_mode_portable',
        'py5',
        tr('py5 mode for portable Thonny'),
        toggle_variable_portable,
        flag_name=_OPTION_PORTABLE,
        group=100
    )
    # non-portable / installed button
    get_workbench().set_default(_OPTION_INSTALLED, False)
    get_workbench().add_command(
        'toggle_py5_mode',
        'py5',
        tr('py5 mode for installed Thonny'),
        toggle_variable_installed,
        flag_name=_OPTION_INSTALLED,
        group=100
    )

