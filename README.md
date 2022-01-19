# thonny-py5mode

*A py5 plug-in for Thonny*

Use the [Thonny Python IDE](https://thonny.org/) as a Processing PDE alternative for creative coding. *Thonny-py5mode* is a plug-in that installs and configures Thonny for use with [py5](http://py5.ixora.io/), a Python (3.8+) framework that leverages Processing's core libraries.

<!--For more on writing py5 code using this plug-in, [check out my CC Fest presentation](https://github.com/tabreturn/cc-fest-py5) on the topic.-->


## Instructions

If you already have some version of Thonny *that includes Python 3.8+* on your computer, you can skip straight to step 4.

1. Download and install the *-alt* version of the Thonny IDE (for Python 3.9 support) from: https://github.com/thonny/thonny/releases/tag/v3.3.7

   ![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/01-download-thonny.png)

2. Start Thonny. If you're running it for the first time, just accept the *Standard* settings.

   ![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/02-start-splash.png)

3. Once Thonny is open, select *Tools > Manage plugins...*

   ![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/03.01-manage-plug-ins.png)

   Then search for and install __thonny-py5mode__ plug-in --

   ![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/03.02-install-plug-in.png)

   You must __restart Thonny__ after this step.

4. When you've restarted Thonny, select *py5 > Imported mode for py5* --

   ![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/04.01-activate-imported-mode.png)

   This will download, extract, and set up JDK-11 for you (if you need to know: the plug-in installs JDK in the Thonny user-config directory). Thonny only needs to download JDK the first time you switch to imported mode. __Thonny will appear to freeze__ for a while when it's downloading JDK (I have plans to develop a proper progress indicator later).

   ![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/04.02-download-jdk.png)

   You'll be notified once the download is done --

   ![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/04.03-download-jdk-done.png)

5. *This step is optional.* There are several Thonny settings that I recommend you apply for working with py5 (including a Processing 4 inspired theme, Kyanite). You can apply those settings in one simple step using  *py5 > Apply recommended py5 settings*

   ![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/05-apply-recommended-settings.png)

6. When the py5 *Imported mode for py5* option is checked, Thonny will run your code (using py5's run_sketch command line tool) --

   ![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/06.01-imported-activated.png)

   Try out an [imported mode](https://py5.ixora.io/content/py5_modes.html#imported-mode) sketch using the green play button (or the F5 or Ctrl+R keyboard shortcuts).

   ```python
   def setup():
       size(300, 200)
       rect_mode(CENTER)

   def draw():
       rect(mouse_x, mouse_y, 10, 10)
   ```

   ![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/06.02-running-sketch.png)

   NOTE: This mode also runs [static mode](https://py5.ixora.io/content/py5_modes.html#static-mode) sketches (when you don't need a `draw()` function for animation).


## Module Mode Sketches

To run a py5 [module mode](https://py5.ixora.io/content/py5_modes.html#module-mode) sketch, deactivate/uncheck *py5 > Imported mode for py5* first so that Thonny returns to its normal run behaviour (for running any Python script). As an example, you can try this code:

```python
import py5

def setup():
    py5.size(200, 200)
    py5.rect_mode(py5.CENTER)

def draw():
    py5.square(py5.mouse_x, py5.mouse_y, 10)

py5.run_sketch()
```

Note that module mode requires an `import py5` and `run_sketch()` line, and `py5.` prefixes for everything.


## Credits

Thanks [villares](https://github.com/villares/thonny-py5-runner) for inspiring me to develop this plug-in, [hx2A](https://github.com/hx2A/) for the awesome [py5 project](https://py5.ixora.io/), and the [Thonny folks](https://github.com/thonny) for their fantastic IDE.


## Todo List

This plug-in is still very much a work in progress ... please report issues [here](https://github.com/tabreturn/thonny-py5mode/issues).

- ~~Integrate alpha version py5 (and JDK) installer~~
- Display download/installation progress in Thonny (not the terminal) -- so Thonny doesn't appear frozen while when it's downloading JDK
- Restorable Thonny settings -- restore applied py5 config (themes, etc.) on deactivate
- ~~Support for non-portable/installed Thonny~~
- Support for portable Thonny?
- ~~Imported mode auto-completion~~
- ~~Processing inspired theme for UI~~
- ~~Processing inspired theme for syntax~~
- ~~Imported mode Syntax highlighting~~
- ~~Pop up built-in save dialog for new unsaved files~~
- ~~Update instructions/readme~~
- Conceal full run_sketch.py run command in Thonny shell?
- Add Processing.py mode (using py5_tools > translators)?
- ...
