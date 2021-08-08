# thonny-py5mode

*A py5 plug-in for Thonny*

Use the [Thonny Python IDE](https://thonny.org/) as a Processing PDE alternative for creative coding. *Thonny-py5mode* is a plug-in that installs and configures Thonny for use with [py5](http://py5.ixora.io/), a Python (3.8+) framework that leverages Processing's core libraries.

This plug-in will work with the portable version of Thonny. It's also likely to work with Thonny versions that include an installer.

**Development on this package has just begun; thonny-py5mode is still in its experimental stages**. It's only tested on Linux right now; it *might* work on Windows. You should be aware that there are a few [py5 issues with Mac (OSX) computers](https://py5.ixora.io/tutorials/mac-users/).

## Instructions

These are instructions for Linux. You'll need to adapt steps 1, 2, 3 for other platforms. Where applicable, there are notes for non-portable/installed versions of Thonny. You can skip straight to step 4 if you already have some version of Thonny *that includes Python 3.8+* on your computer.

1. Download the *-alt* version of the Thonny IDE (for Python 3.9 support) from: https://github.com/thonny/thonny/releases/tag/v3.3.7 (grab *thonny-3.3.7-x86_64-alt.tar.gz* for Linux)
   
   ![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/01-download.png)

2. Extract this archive and place the *thonny* folder wherever you like on your computer (this runs as a portable app, no installer required).

3. In the newly-extracted thonny folder, locate and run `bin/thonny`.
   
   ![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/03.01-extract-and-run.png)
   
   If you're running Thonny for the first time, just accept the default *Standard* settings.
   
   ![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/03.02-splash.png)

4. Once Thonny is open, select *Tools > Manage plugins...*
   
   ![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/04.01-manage-plug-ins.png)
   
   Then search for and install __thonny-py5mode__ (note you'll need to restart Thonny after this step).
   
   ![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/04.02-install-plug-in.png)

5. When you've restarted Thonny, select *py5 > Activate py5 mode for Thonny* -- this will download and extract JDK-11 into the Thonny user-config directory (`~/.config/Thonny` on Linux). You'll have to activate this mode when you want to use py5 (but the download only happens on the first occasion).
   
   ![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/05.01-activate-py5-mode.png)
   
   NOTE: Thonny will appear to freeze for a while when it's downloading JDK (the plug-in needs a proper progress indicator) --
   
   ![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/05.02-jdk-download.png)
   
   But, you'll be notified once the download is done.
   
   ![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/05.03-jdk-ready.png)

<!--
5. When you've restarted Thonny, select *py5 > Activate py5 mode for Thonny* -- this will download and extract JDK-11 into the Thonny user-config directory (`~/.config/Thonny` on Linux). You'll have to activate this mode every time you want to use py5 (but the download only happens on the first occasion).
   
   ![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/portable-05.01-activate-py5-mode.png)
   
   **For a non-portable/installed version of Thonny**, use *py5 > py5 mode for installed Thonny* to install JDK-11 in the Thonny user-config directory (`~/.config/Thonny` on Linux).
   
   NOTE: Thonny will appear to freeze for a while as it carries out this task (the plug-in needs a proper progress indicator) --
   
   ![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/05.02-jdk-download.png)
   
   But, you'll be notified once it's done.
   
   ![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/05.03-jdk-ready.png)
-->

6. Try out an [imported mode](https://py5.ixora.io/tutorials/py5-modes/#module-mode) sketch using *py5 > Run imported mode sketch* (or using Ctrl+U).

   ```python
   def setup():
       size(500, 500)
       fill(255, 0, 0)
       no_stroke()
   
   def draw():
   circle(mouse_x, mouse_y, 10)
   ```
   
   ![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/06-run-imported-mode.png)
   <!-- ![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/portable-06-run-imported-mode.png) -->
   
   NOTE: you'll need to save your sketch (*File > Save as...*) somewhere first. After that, Thonny saves the file for you each time you run it.


## Module Mode Sketches

You can run a py5 [module mode](https://py5.ixora.io/tutorials/py5-modes/#module-mode) sketch using the standard Thonny run menu (*Run > Run current script*). Be sure to *py5 > Activate py5 mode for Thonny* (this should be checked). As an example, you can try this code:

```python
import py5

def setup():
    py5.size(200, 200)
    py5.rect_mode(py5.CENTER)

def draw():
    py5.square(py5.mouse_x, py5.mouse_y, 10)

py5.run_sketch()
```

<!--
## Keeping Thonny Portable

You may prefer your packages installed in the thonny app folder -- this is neat because you end up with a portable version of Thonny that includes everything to run py5!

The Thonny plug-in (and package) manager will install packages on Linux to `/home/user/.local/lib/`. To use your Thonny app folder instead, select *Tools > Open system shell...* -- this will open a terminal window with a list of `pip` commands. Use the one located in your thonny folder (see image below). In other words, enter `pip3 install thonny-py5mode` to install the plug-in.

![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/terminal_pip.png)

BUT: sometimes the terminal doesn't show the Thonny commands. In this case, you can open a terminal (from outside Thonny) and `cd` to your `thonny/bin` directory, then enter `./pip3 install thonny-py5mode` to use the pip version that targets the bundled Thonny interpreter.
-->


## Credits

I was inspired to get started on this by [villares' experiment](https://github.com/villares/thonny-py5-runner), and thonny-py5mode will likely end up integrated into this.

If you're interested in Python for creative coding and don't know about [hx2A's](https://github.com/hx2A) py5 project, you need to check it out now!


## Todo List

- ~~Get started~~
- ~~Add tickable/toggled menu option~~
- ~~Add support for non-portable/installed version of Thonny~~
- Display download/installation progress in Thonny (not the terminal)
- ~~Add support for [py5 imported mode](http://py5.ixora.io/tutorials/py5-modes/#imported-mode)~~
- Fix portable mode
- Auto-completion for module mode
- Highlighting for py5 code
- ...
