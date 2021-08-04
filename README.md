# thonny-py5mode

*A py5 plug-in for Thonny*

This plugin is designed to work with the portable version of Thonny. It's also likely to work with those versions that include an installer.

**Development on this package has just begun; thonny-py5mode is still in its experimental stages**. I've only tested this on Linux right now.

## Instructions

1. Download the *-alt* version of the Thonny IDE (for Python 3.9 support) from: https://github.com/thonny/thonny/releases/tag/v3.3.7 (grab *thonny-3.3.7-x86_64-alt.tar.gz* for Linux)

2. Extract this archive and place the *thonny* folder wherever you like (this runs as a portable app, no installer required).

3. In the thonny folder, locate and run `bin/thonny` (preferably from your terminal whenever you start Thonny, so you can see thonny-py5mode logging messages).

4. Once Thonny is open, select *Tools > Manage plug-ins...*, then search for and install __thonny-py5mode__ (note you'll need to restart Thonny after this step).

5. Once you've restarted Thonny (from your terminal?), select *Tools > Activate py5 mode* (this'll download and extract JDK-11 into `thonny/bin/jdk-11` and set `JAVA_HOME` to that path).

6. Try out a sketch (note I haven't programmed 'imported mode' support yet):

```python
def setup():
    py5.size(200, 200)
    py5.rect_mode(py5.CENTER)

def draw():
    py5.square(py5.mouse_x, py5.mouse_y, 10)

py5.run_sketch()
```

I'm basically trying to automate this process:  
https://tabreturn.github.io/code/python/thonny/2021/06/21/thonny_and_py5.html

**You may prefer your packages installed in the thonny app folder -- this is neat because you end up with a portable version of Thonny that includes everything to run py5!** The Thonny plug-in (and package) manager will install packages to `/home/user/.local/lib/`. To use your Thonny app folder instead, use *Tools > Open system shell...* -- this will open a terminal window with a list of `pip` commands. Use the one located in your thonny folder (see image below). In other words, enter `pip3 install thonny-py5mode` to install the plugin.

![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/terminal_pip.png)

I was inspired to get started on this by [villares' experiment](https://github.com/villares/thonny-py5-runner), and thonny-py5mode will likely end up integrated into this.

If you're interested in Python for creative coding and don't know about [hx2A's](https://github.com/hx2A) py5 project, you need to check it out now!

## todo list

- ~~Get started~~
- Display download/installation progress in Thonny (not the terminal)
- Add support for [py5 imported mode](http://py5.ixora.io/tutorials/py5-modes/#imported-mode)
- Buttons and indicators! How does one switch between modes using Thonny; how is this reflected in the interface?
- ...
