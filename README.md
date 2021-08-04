# thonny-py5mode

*A py5 plugin for Thonny*

This plugin is designed to work with the portable version of Thonny.

**Development on this package has just begun; thonny-py5mode still its experimental stages**

1. Download the *-alt* version of the Thonny IDE (for Python 3.9 support): https://github.com/thonny/thonny/releases/download/v3.3.7/thonny-3.3.7-x86_64-alt.tar.gz

2. Extract this archive and place the *thonny* folder wherever you like (this runs like a portable app, no installer required).

3. Open your terminal and `cd` to `thonny/bin/`; download this repo into that directory and run `./pip3 thonny-py5mode` (which uses the pip that ships with Thonny to install packages for the bundled Python interpreter).

4. Run `thonny/bin/thonny` (preferably from your terminal so that you can see the plugin logging messages).

5. In Thonny, select *Tools > py5* (this'll download and extract JDK-11 into `thonny/bin/jdk-11` and set `JAVA_HOME` to that path).

6. Try out a sketch (I haven't programmed 'imported mode' support yet):

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

I was inspired to get started on this by [villares](https://github.com/villares/thonny-py5-runner), and it'll likely end up integrated into this: https://github.com/villares/thonny-blue-code-format

If you're interested in Python for creative coding, and don't know about [hx2A's](https://github.com/hx2A) py5 project, you need to check it out now!

\* Only testing this on Linux right now

## todo list

- [x] get started
- [ ] lots more ...
