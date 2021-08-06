'''
thonny-py5mode.

py5 plugin for Thonny.

# NOTES TO SELF:
* documentation: https://github.com/thonny/thonny/wiki/Plugins
* maybe look at how Run > Pygame Zero Mode is programmed?
'''

__author__ = 'tabreturn'
__credits__ = 'organisation name'


import os, pathlib, sys
# for jdk downloader (https://pypi.org/project/install-jdk/)
import jdk, threading, time
# thonny plugin imports
from thonny import get_workbench
from thonny.languages import tr
from tkinter.messagebox import showinfo


def setJAVA_HOME():
    ''' set jdk path to thonny/lib/jdk-11 '''
    jdk = pathlib.Path(sys.executable).parents[1] / 'lib' / 'jdk-11'
    os.environ['JAVA_HOME'] = str(jdk)


def activatePy5():
    ''' get thonny (portable version) paths '''
    thonny_interpreter = pathlib.Path(sys.executable)
    thonny_root = pathlib.Path(thonny_interpreter).parents[1]
    thonny_lib = thonny_root / 'lib'

    if not pathlib.Path(thonny_lib / 'jdk-11').exists():
        print('py5 requires jdk-11')

        def display_progress(task):
            ''' progress indicator for downloading jdk '''
            print(msg)
            progress = '> ·'
            while not progress_complete:
                print(progress)
                progress += '-'
                time.sleep(1)

        # download jdk
        progress_complete = False
        msg = '> downloading jdk '
        dl_thread = threading.Thread(target=display_progress, args=(msg,))
        dl_thread.start()
        jdk_file = jdk._download(jdk.get_download_url('11'))
        progress_complete = True

        # extract jdk to thonny's thonny/lib/
        print('> extracting jdk')
        jdk._USER_DIR = thonny_root
        jdk_ext = jdk._get_normalized_compressed_file_ext(jdk_file)
        jdk_dir = jdk._decompress_archive(jdk_file, jdk_ext, thonny_lib)
        
        # rename extracted jdk directory to thonny/lib/jdk-11
        lib_path = pathlib.Path(thonny_lib)
        for name in os.listdir(lib_path):
            if name.startswith('jdk-11'):
                os.rename(lib_path / name, lib_path / 'jdk-11')
                print('> done!')
                setJAVA_HOME()
                return 'JDK-11 installed and JAVA_HOME set'

    else:
        # set jdk path to thonny/lib/jdk-11
        setJAVA_HOME()
        return 'JAVA_HOME set'


_OPTION_NAME = 'run.py5_mode'


def toggle_variable():
    var = get_workbench().get_variable(_OPTION_NAME)
    var.set(not var.get())
    update_environment()

    if var.get():
        # activate py5 (and download jdk if necessary) 
        showinfo(activatePy5(), 'py5 mode activated')


def update_environment():
    if get_workbench().in_simple_mode():
        os.environ['PY5_MODE'] = 'auto'
    else:
        os.environ['PY5_MODE'] = str(get_workbench().get_option(_OPTION_NAME))


def load_plugin():
    get_workbench().set_default(_OPTION_NAME, False)
    get_workbench().add_command(
      'toggle_py5_mode',
      'tools',
      tr('py5 mode'),
      toggle_variable,
      flag_name=_OPTION_NAME,
      group=180,
    )
