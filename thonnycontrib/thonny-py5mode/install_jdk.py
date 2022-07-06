'''thonny-py5mode jdk installer
   checks for jdk and, if not found, installs it to the thonny config directory
'''

import jdk
import os
import pathlib
import threading
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from thonny import get_workbench, THONNY_USER_DIR, ui_utils
from thonny.languages import tr


_REQUIRE_JDK = 17
_INSTALL_JDK_MESSAGE = '''Thonny requires JDK to run py5 sketches. \
It\'ll need to download about 180 MB.'''


class DownloadJDK(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self) -> str:
        '''download and setup jdk (installs to thonny config directory)'''
        jdk_dir = 'jdk-' + str(_REQUIRE_JDK)

        system_jdk = 'TBD'
        # check system for existing jdk install (and the version number)
        if os.environ.get('JAVA_HOME') is not None:
            jdk_ver = os.environ['JAVA_HOME'].split('jdk-')[-1].split('.')[0]
            system_jdk = jdk_ver

        for name in os.listdir(THONNY_USER_DIR):
            # check for jdk in thonny config directory
            if name.startswith(jdk_dir):
                # set jdk path to thonny config directory
                set_java_home(pathlib.Path(THONNY_USER_DIR) / jdk_dir)
                return 'JAVA_HOME set'

        if not system_jdk.isdigit() or int(system_jdk) < _REQUIRE_JDK:
            print('> py5 requires jdk-%d' % _REQUIRE_JDK)

            for name in os.listdir(THONNY_USER_DIR):
                # delete existing thonny-py5mode jdk (if one exists)
                if name.startswith(jdk_dir):
                    shutil.rmtree(pathlib.Path(install_to) / name)
            # download jdk
            jdk_file = jdk._download(jdk.get_download_url(_REQUIRE_JDK))
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
                    return 'All done! py5 is ready.'
                    break

            set_java_home(pathlib.Path(THONNY_USER_DIR) / dest)
            # one-off env var, so no need to restart thonny on jdk install
            os.environ['JAVA_HOME'] = str(pathlib.Path(THONNY_USER_DIR) / dest)

            return f'JDK-{_REQUIRE_JDK} installed and JAVA_HOME set'

        # set jdk path to thonny config directory
        set_java_home(pathlib.Path(THONNY_USER_DIR) / jdk_dir)
        return 'JAVA_HOME set'


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
        self.ok_button.grid(row=3, column=0, padx=15, pady=15, sticky='w')
        self.ok_button.focus_set()
        # cancel button
        self.cancel_button = ttk.Button(
          self.main_frame,
          text='Cancel',
          command=self._close
        )
        self.cancel_button.grid(row=3, column=1, padx=15, pady=15, sticky='e')


    def _proceed(self, event=None) -> None:
        '''start jdk downloader thread'''
        self.ok_button.destroy()
        self.cancel_button.destroy()
        # progressbar
        self.progress_bar = ttk.Progressbar(
          self.main_frame, orient=tk.HORIZONTAL, mode='indeterminate')
        self.progress_bar.grid(
          row=2, column=0, columnspan=2, sticky=tk.EW, padx=15, pady=(0,15))

        self.start_downloading()
        download_thread = DownloadJDK()
        download_thread.start()
        self.monitor(download_thread)

    def _close(self) -> None:
        '''cancel without starting jdk downloader thread'''
        self.destroy()

    def start_downloading(self) -> None:
        self.main_frame.tkraise()
        self.progress_bar.start(20)

    def stopped_downloading(self) -> None:
        self.progress_bar.stop()

    def monitor(self, download_thread) -> None:
        if download_thread.is_alive():
            self.after(100, lambda: self.monitor(download_thread))
        else:
            self.stopped_downloading()
            self.destroy()
            showinfo('title', 'done', master=workbench)
            print('stop dling')


def set_java_home(jdk_path: pathlib.Path) -> None:
    '''add jdk path to config file (tools > options > general > env vars)'''
    jdk_path = 'JAVA_HOME=' + str(jdk_path)
    env_vars = get_workbench().get_option('general.environment')

    if jdk_path not in env_vars:
        env_vars.append(jdk_path)

    get_workbench().set_option('general.environment', env_vars)


def install_jdk() -> None:
    '''call from where this module is imported'''
    ui_utils.show_dialog(JdkDialog(get_workbench()))
