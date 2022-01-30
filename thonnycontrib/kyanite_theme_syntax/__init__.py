'''kyanite syntax theme
   theme inspired by processing 4.0b3 default theme, kyanite
'''

from thonny import get_workbench, workbench


def kyanite_syntax() -> workbench.SyntaxThemeSettings:
    '''based on default_light (see thonny > plugins > base_syntax_themes)'''
    default_fg = '#111155'
    default_bg = '#FFFFF2'
    light_fg = '#94A4AF'
    string_fg = '#7D4793'
    open_string_bg = '#E2E7E1'
    gutter_foreground = '#A4B4BF'
    gutter_background = '#E2E7E1'

    return {
      'TEXT': {
        'foreground': default_fg,
        'insertbackground': default_fg,
        'background': default_bg,
      },
      'GUTTER': {
        'foreground': gutter_foreground,
        'background': gutter_background
      },
      'breakpoint': {'foreground': 'crimson'},
      'current_line': {'background': '#D9FAFF'},
      'definition': {'foreground': '#006699', 'font': 'BoldEditorFont'},
      'string': {'foreground': string_fg},
      'string3': {
        'foreground': string_fg,
        'background': None, 'font': 'EditorFont'
      },
      'open_string': {'foreground': string_fg, 'background': open_string_bg},
      'open_string3': {
        'foreground': string_fg,
        'background': open_string_bg,
        'font': 'EditorFont',
      },
      'tab': {'background': '#F5ECD7'},
      'keyword': {'foreground': '#33997E', 'font': 'EditorFont'},
      'builtin': {'foreground': '#006699'},
      'number': {'foreground': '#B04600'},
      'comment': {'foreground': light_fg},
      'welcome': {'foreground': light_fg},
      'magic': {'foreground': light_fg},
      'prompt': {'foreground': string_fg, 'font': 'BoldEditorFont'},
      'stdin': {'foreground': 'Blue'},
      'stdout': {'foreground': 'Black'},
      'stderr': {'foreground': '#CC0000'},  # same as ANSI red
      'value': {'foreground': 'DarkBlue'},
      'hyperlink': {'foreground': '#3A66DD', 'underline': True}
    }


def load_plugin() -> None:
    get_workbench().add_syntax_theme(
      'Kyanite Syntax',
      'Default Light',
      kyanite_syntax
    )
