'''thonny-py5mode jdk installer
   checks for jdk and, if not found, installs it to the thonny config directory
'''

import jdk
import os
import pathlib
import threading
import tkinter as tk
from thonny import get_workbench, THONNY_USER_DIR, ui_utils
from thonny.languages import tr
from tkinter import ttk
from tkinter.messagebox import showinfo


_REQUIRE_JDK = 17
_INSTALL_JDK_MESSAGE = '''Thonny requires JDK to run py5 sketches. \
It\'ll need to download about 180 MB.'''


def jdk_install_exists() -> bool:
    '''
    Look for a jdk in Thonny's user directory first, and if one is present,
    set up JAVA_HOME, add it to Thonny's options, and return True. Otherwise,
    look for existing JAVA_HOME pointing to a jdk that meets the py5 version
    requirements and return True/False accordingly.
    '''
    # search for jdk in Thonny's user config directory
    jdk_dir = 'jdk-' + str(_REQUIRE_JDK)
    for name in os.listdir(THONNY_USER_DIR):
        if name.startswith(jdk_dir):
            # set JAVA_HOME in Thonny's config (and in current env) with jdk_dir path 
            set_java_home(pathlib.Path(THONNY_USER_DIR) / jdk_dir)
            return True    
    # check system for existing jdk install (and the version number)
    system_jdk = 'TBD'
    if os.environ.get('JAVA_HOME') is not None:
        jdk_ver = os.environ['JAVA_HOME'].split('jdk-')[-1].split('.')[0]
        system_jdk = jdk_ver
    # False if no JAVA_HOME was set, or if it is not the required version
    return system_jdk.isdigit() and int(system_jdk) >= _REQUIRE_JDK     


def set_java_home(jdk_path: pathlib.Path) -> None:
    '''
    Add jdk path to current envirnonment and to Thonny's config file
    as visible in (tools > options > general > env vars)
    '''
    os.environ['JAVA_HOME'] = str(pathlib.Path(THONNY_USER_DIR) / jdk_path)
    java_home_var = 'JAVA_HOME=' + str(jdk_path)
    env_vars = get_workbench().get_option('general.environment')
    for i, env_var in enumerate(env_vars):
        if 'JAVA_HOME' in env_var:
           env_vars[i] = java_home_var
           break
    else:
        env_vars.append(java_home_var)
    get_workbench().set_option('general.environment', env_vars)

class DownloadJDK(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self) -> None:
        '''download and setup jdk (installs to thonny config directory)'''
        jdk_dir = 'jdk-' + str(_REQUIRE_JDK)

        for name in os.listdir(THONNY_USER_DIR):
            # delete existing thonny-py5mode jdk (if one exists)
            if name.startswith(jdk_dir):
                shutil.rmtree(pathlib.Path(install_to) / name)

        # download and extract jdk
        jdk.install(_REQUIRE_JDK, path=THONNY_USER_DIR)

        for name in os.listdir(THONNY_USER_DIR):
            # rename extracted jdk directory to jdk-<version#>
            if name.startswith(jdk_dir):
                src = pathlib.Path(THONNY_USER_DIR) / name
                dest = pathlib.Path(THONNY_USER_DIR) / jdk_dir
                os.rename(src, dest)
                print('> rename extracted jdk')
                break

        # set java_home
        print('> set java_home')
        set_java_home(pathlib.Path(THONNY_USER_DIR) / dest)
        os.environ['JAVA_HOME'] = str(pathlib.Path(THONNY_USER_DIR) / dest)
        print('> done')


class JdkDialog(ui_utils.CommonDialog):
    def __init__(self, master):
        super().__init__(master)
        # window/frame
        self.main_frame = ttk.Frame(self)
        self.main_frame.grid(sticky=tk.NSEW, ipadx=15, ipady=15)
        self.main_frame.rowconfigure(0, weight=1)
        self.main_frame.columnconfigure(0, weight=1)
        self.title(tr('Install JDK for py5'))
        self.resizable(height=tk.FALSE, width=tk.FALSE)
        self.protocol("WM_DELETE_WINDOW", lambda: None)
        # install message
        message_label = ttk.Label(self.main_frame, text=_INSTALL_JDK_MESSAGE)
        message_label.grid(pady=0, columnspan=2)
        # ok button
        self.ok_button = ttk.Button(
          self.main_frame,
          text=tr('Proceed'),
          command=self._proceed,
          default='active'
        )
        self.ok_button.grid(row=2, column=0, padx=15, pady=15, sticky='w')
        self.ok_button.focus_set()
        # cancel button
        self.cancel_button = ttk.Button(
          self.main_frame,
          text='Cancel',
          command=self._close
        )
        self.cancel_button.grid(row=2, column=1, padx=15, pady=15, sticky='e')

    def _proceed(self, event=None) -> None:
        '''start jdk downloader thread'''
        self.ok_button.destroy()
        self.cancel_button.destroy()
        # progress bar label
        msg = f'Downloading and extracting JDK {_REQUIRE_JDK} ...'
        dl_label = ttk.Label(self.main_frame, text=msg)
        dl_label.grid(row=1, columnspan=2, pady=(0, 15))
        # progress bar
        self.progress_bar = ttk.Progressbar(
          self.main_frame, orient=tk.HORIZONTAL, mode='indeterminate')
        self.progress_bar.grid(
          row=2, column=0, columnspan=2, padx=15, pady=(0, 15), sticky='ew')
        # start progress bar animation and download thread
        self.main_frame.tkraise()
        self.progress_bar.start(20)
        download_thread = DownloadJDK()
        download_thread.start()
        self.monitor(download_thread)

    def _close(self) -> None:
        '''cancel without starting jdk downloader thread'''
        self.destroy()

    def monitor(self, download_thread) -> None:
        '''animate progress bar while jdk installs and extracts'''
        if download_thread.is_alive():
            self.after(100, lambda: self.monitor(download_thread))
        else:
            self.progress_bar.stop()
            self.destroy()
            msg = f'JDK {_REQUIRE_JDK} extracted to {THONNY_USER_DIR}\n\n'
            msg += 'You can now run py5 sketches.'
            showinfo('JDK done', msg, master=get_workbench())


def install_jdk() -> None:
    '''call this function from where this module is imported'''
    if not jdk_install_exists():
        ui_utils.show_dialog(JdkDialog(get_workbench()))

