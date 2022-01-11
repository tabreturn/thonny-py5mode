1. Added py5 imported mode support (site-packages/thonny/running.py)
   ```python
   if args and args[0] == 'py5_imported_mode':
       import site
       rs_file = '/py5_tools/tools/run_sketch.py'
       rs_path = os.path.abspath(site.getsitepackages()[0] + rs_file)
       cmd_parts = ["%" + command_name, rs_path, rel_filename]
   ```
2. Configured some default Thonny options (site-packages/thonny/default.ini)
  * `[view] ui_theme = Clean Dark Blue`
  * `[view] syntax_theme = Tomorrow`
  * `[run] program_arguments = py5_imported_mode`
  * `[assistance] open_assistant_on_errors = False`

3. Added py5 syntax coloring (site-packages/thonny/token_utils.ini)
  * `import py5; _builtinlist += dir(py5)`

5. Added py5 autocompletion (site-packages/thonny/jedi_utils.ini > get_script_completions)
  * `source = 'from py5 import *;' + source`

4. Cleaned up
  * `py3clean .`

