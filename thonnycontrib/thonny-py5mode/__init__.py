'''
thonny-py5mode.

py5 plugin for Thonny.
'''

__version__ = "0.0.1"
__author__ = 'author name'
__credits__ = 'organisation name'


import os, pathlib, sys
# for jdk downloader (https://pypi.org/project/install-jdk/)
import itertools, jdk, threading, time


def setJAVA_HOME():
    # set jdk path to thonny/lib/jdk-11
    jdk = pathlib.Path(sys.executable).parents[1] / 'lib' / 'jdk-11'
    os.environ['JAVA_HOME'] = str(jdk)


def activatePy5():
    # get thonny (portable version) paths
    thonny_interpreter = pathlib.Path(sys.executable)
    thonny_root = pathlib.Path(thonny_interpreter).parents[1]
    thonny_lib = thonny_root / 'lib'

    if not pathlib.Path(thonny_lib / 'jdk-11').exists():
        sys.stdout.write('\npy5 requires jdk-11')
        sys.stdout.write('\nplease wait a moment while this installs\n')
        
        # progress indicator for downloading jdk
        def display_progress(task):
            progress = '.'
            while not progress_complete:
                sys.stdout.write(task + progress)
                sys.stdout.flush()
                progress += '.'
                time.sleep(0.1)

        # download jdk
        progress_complete = False
        msg = '\r> downloading jdk '
        dl_thread = threading.Thread(target=display_progress, args=(msg,))
        dl_thread.start()
        jdk_file = jdk._download(jdk.get_download_url('11'))
        progress_complete = True

        # extract jdk to thonny's thonny/lib/
        sys.stdout.write('\n> extracting jdk')
        jdk._USER_DIR = thonny_root
        jdk_ext = jdk._get_normalized_compressed_file_ext(jdk_file)
        jdk_dir = jdk._decompress_archive(jdk_file, jdk_ext, thonny_lib)
        
        # rename extracted jdk directory to thonny/lib/jdk-11
        lib_path = pathlib.Path(thonny_lib)
        for name in os.listdir(lib_path):
            if name.startswith('jdk-11'):
                os.rename(lib_path / name, lib_path / 'jdk-11')
                sys.stdout.write('\n> done!\n')
                setJAVA_HOME()
                return 'JDK-11 installed and JAVA_HOME set'

    else:
        # set jdk path to thonny/lib/jdk-11
        setJAVA_HOME()
        return 'JAVA_HOME set'


# NOTES TO SELF:
# documentation: https://github.com/thonny/thonny/wiki/Plugins
# maybe look at how Run > Pygame Zero Mode is programmed?


from thonny import get_workbench
from tkinter.messagebox import showinfo


def test():
    #showinfo("Hello!", "Thonny rules!")
    showinfo('Py5 ready!', activatePy5())


def load_plugin():
    get_workbench().add_command(command_id="py5",
                                menu_name="tools",
                                command_label="py5",
                                handler=test)
