'''
thonny-py5mode.

py5 plugin for Thonny.

# NOTES TO SELF:
* documentation: https://github.com/thonny/thonny/wiki/Plugins
* maybe look at how Run > Pygame Zero Mode is programmed?
'''

__author__ = 'tabreturn'
__credits__ = 'organisation name'


import os, pathlib, shutil, sys
# for jdk downloader (https://pypi.org/project/install-jdk/)
import jdk, threading, time
# thonny plugin imports
from thonny import get_workbench, THONNY_USER_DIR
from thonny.languages import tr
from tkinter.messagebox import showinfo


def set_JAVA_HOME(jdk_path):
    ''' set jdk path to thonny/lib/jdk-11 '''
    os.environ['JAVA_HOME'] = str(jdk_path)


def activate_py5(install_type):
    ''' get thonny (portable version) paths '''
    require_jdk = 11
    jdk_dir = 'jdk-' + str(require_jdk)
    no_jdk_dir = True
    # install to thonny app directory if portable
    if install_type == 'portable': thonny_root = sys.path[0]
    # install to thonny user config directory if non-portable
    if install_type == 'installed': thonny_root = THONNY_USER_DIR

    system_jdk = os.environ['JAVA_HOME'].split('jdk-')[-1].split('.')[0]

    for name in os.listdir(thonny_root):
        # check for jdk directory thonny app / config directory
        if name.startswith(jdk_dir):
            no_jdk_dir = False

    if no_jdk_dir or not system_jdk.isdigit() or int(system_jdk) < require_jdk:
        print('> py5 requires jdk-11')

        for name in os.listdir(thonny_root):
            # delete existing *thonny-py5mode jdk*
            if name.startswith(jdk_dir):
                shutil.rmtree(pathlib.Path(thonny_root) / name)

        def display_progress(task):
            ''' progress indicator for downloading jdk '''
            print(msg)
            progress = '·'
            while not progress_complete:
                print(msg + progress)
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
        jdk._USER_DIR = thonny_root
        jdk_ext = jdk._get_normalized_compressed_file_ext(jdk_file)
        ext_jdk = jdk._decompress_archive(jdk_file, jdk_ext, thonny_root)

        for name in os.listdir(thonny_root):
            # rename extracted jdk directory to jdk-11
            if name.startswith(jdk_dir):
                src = pathlib.Path(thonny_root) / name
                dest = pathlib.Path(thonny_root) / jdk_dir
                os.rename(src, dest)
                print('> done!')
                break

        set_JAVA_HOME(pathlib.Path(thonny_root) / dest)
        return 'JDK-11 installed and JAVA_HOME set'

    else:
        # set jdk path to thonny app / config directory
        set_JAVA_HOME(pathlib.Path(thonny_root) / jdk_dir)
        return 'JAVA_HOME set'


_OPTION_PORTABLE = 'run.py5_mode_portable'
def toggle_variable_portable(): toggle_variable('portable')

_OPTION_INSTALLED = 'run.py5_mode_installed'
def toggle_variable_installed(): toggle_variable('installed')


def toggle_variable(install_type):
    ''' install_type is portable or installed '''
    var_portable = get_workbench().get_variable(_OPTION_PORTABLE)
    var_installed = get_workbench().get_variable(_OPTION_INSTALLED)

    if install_type == 'portable':
        var_installed.set(False)
        var_portable.set(not var_portable.get())

    if install_type == 'installed':
        var_portable.set(False)
        var_installed.set(not var_installed.get())

    ''' DON'T KNOW WHAT THIS IS FOR
    if get_workbench().in_simple_mode():
        os.environ['PY5_MODE'] = 'auto'
    else:
        os.environ['PY5_MODE'] = str(get_workbench().get_option(_OPTION_PORTABLE))
    '''
    if var_portable.get() or var_installed.get():
        # activate py5 (and download jdk if necessary)
        showinfo(activate_py5(install_type), 'py5 mode activated')


def load_plugin():
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

