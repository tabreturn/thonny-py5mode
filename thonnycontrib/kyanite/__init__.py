# theme based on Processing 4.0b3 default theme, kyanite

from thonny import get_workbench
from thonny.workbench import SyntaxThemeSettings


def kyanite_syntax() -> SyntaxThemeSettings:
    default_fg = "#000000"
    default_bg = "#FFFFF2"
    light_fg = "#d9faff"
    string_fg = "#aaf8ff"
    open_string_bg = "#c3f9d3"
    gutter_foreground = "#999999"
    gutter_background = "#e0e0e0"

    return {
        "TEXT": {
            "foreground": default_fg,
            "insertbackground": default_fg,
            "background": default_bg,
        },
        "GUTTER": {"foreground": gutter_foreground, "background": gutter_background},
        "breakpoint": {"foreground": "crimson"},
        "current_line": {"background": "#f5f5f5"},
        "definition": {"foreground": "DarkBlue", "font": "BoldEditorFont"},
        "string": {"foreground": string_fg},
        "string3": {"foreground": string_fg, "background": None, "font": "EditorFont"},
        "open_string": {"foreground": string_fg, "background": open_string_bg},
        "open_string3": {
            "foreground": string_fg,
            "background": open_string_bg,
            "font": "EditorFont",
        },
        "tab": {"background": "#f5ecd7"},
        "keyword": {"foreground": "#7f0055", "font": "BoldEditorFont"},
        "builtin": {"foreground": "#7f0055"},
        "number": {"foreground": "#B04600"},
        "comment": {"foreground": light_fg},
        "welcome": {"foreground": light_fg},
        "magic": {"foreground": light_fg},
        "prompt": {"foreground": "purple", "font": "BoldEditorFont"},
        "stdin": {"foreground": "Blue"},
        "stdout": {"foreground": "Black"},
        "stderr": {"foreground": "#CC0000"},  # same as ANSI red
        "value": {"foreground": "DarkBlue"},
        "hyperlink": {"foreground": "#3A66DD", "underline": True},
        # paren matcher
        "surrounding_parens": {"foreground": "Blue", "font": "BoldEditorFont"},
        "unclosed_expression": {"background": "LightGray"},
        # find/replace
        "found": {"foreground": "blue", "underline": True},
        "current_found": {"foreground": "white", "background": "red"},
        "matched_name": {"background": "#e6ecfe"},
        "local_name": {"font": "ItalicEditorFont"},
        # debugger
        "active_focus": {"background": "#F8FC9A", "borderwidth": 1, "relief": "solid"},
        "suspended_focus": {"background": "", "borderwidth": 1, "relief": "solid"},
        "completed_focus": {"background": "#BBEDB2", "borderwidth": 1, "relief": "flat"},
        "exception_focus": {"background": "#FFBFD6", "borderwidth": 1, "relief": "solid"},
        "expression_box": {"background": "#DCEDF2", "foreground": default_fg},
        "black_fg": {"foreground": "#2E3436"},
        "black_bg": {"background": "#2E3436"},
        "bright_black_fg": {"foreground": "#555753"},
        "bright_black_bg": {"background": "#555753"},
        "dim_black_fg": {"foreground": "#1E2224"},
        "dim_black_bg": {"background": "#1E2224"},
        "red_fg": {"foreground": "#CC0000"},
        "red_bg": {"background": "#CC0000"},
        "bright_red_fg": {"foreground": "#EF2929"},
        "bright_red_bg": {"background": "#EF2929"},
        "dim_red_fg": {"foreground": "#880000"},
        "dim_red_bg": {"background": "#880000"},
        "green_fg": {"foreground": "#4E9A06"},
        "green_bg": {"background": "#4E9A06"},
        "bright_green_fg": {"foreground": "#8AE234"},
        "bright_green_bg": {"background": "#8AE234"},
        "dim_green_fg": {"foreground": "#346704"},
        "dim_green_bg": {"background": "#346704"},
        "yellow_fg": {"foreground": "#C4A000"},
        "yellow_bg": {"background": "#C4A000"},
        "bright_yellow_fg": {"foreground": "#FCE94F"},
        "bright_yellow_bg": {"background": "#FCE94F"},
        "dim_yellow_fg": {"foreground": "#836B00"},
        "dim_yellow_bg": {"background": "#836B00"},
        "blue_fg": {"foreground": "#3465A4"},
        "blue_bg": {"background": "#3465A4"},
        "bright_blue_fg": {"foreground": "#729FCF"},
        "bright_blue_bg": {"background": "#729FCF"},
        "dim_blue_fg": {"foreground": "#22436D"},
        "dim_blue_bg": {"background": "#22436D"},
        "magenta_fg": {"foreground": "#75507B"},
        "magenta_bg": {"background": "#75507B"},
        "bright_magenta_fg": {"foreground": "#AD7FA8"},
        "bright_magenta_bg": {"background": "#AD7FA8"},
        "dim_magenta_fg": {"foreground": "#4E3552"},
        "dim_magenta_bg": {"background": "#4E3552"},
        "cyan_fg": {"foreground": "#06989A"},
        "cyan_bg": {"background": "#06989A"},
        "bright_cyan_fg": {"foreground": "#34E2E2"},
        "bright_cyan_bg": {"background": "#34E2E2"},
        "dim_cyan_fg": {"foreground": "#046567"},
        "dim_cyan_bg": {"background": "#046567"},
        "white_fg": {"foreground": "#D3D7CF"},
        "white_bg": {"background": "#D3D7CF"},
        "bright_white_fg": {"foreground": "#EEEEEC"},
        "bright_white_bg": {"background": "#EEEEEC"},
        "dim_white_fg": {"foreground": "#8D8F8A"},
        "dim_white_bg": {"background": "#8D8F8A"},
        "fore_fg": {"foreground": default_fg},
        "fore_bg": {"background": default_fg},
        "bright_fore_fg": {"foreground": "#000000"},
        "bright_fore_bg": {"background": "#000000"},
        "dim_fore_fg": {"foreground": "#222222"},
        "dim_fore_bg": {"background": "#222222"},
        "back_fg": {"foreground": default_bg},
        "back_bg": {"background": default_bg},
        "bright_back_fg": {"foreground": "#ffffff"},
        "bright_back_bg": {"background": "#ffffff"},
        "dim_back_fg": {"foreground": "#e0e0e0"},
        "dim_back_bg": {"background": "#e0e0e0"},
        "intense_io": {"font": "BoldIOFont"},
        "italic_io": {"font": "ItalicIOFont"},
        "intense_italic_io": {"font": "BoldItalicIOFont"},
        "underline": {"underline": True},
        "strikethrough": {"overstrike": True},
    }































'''
def kyanite_ui() -> BasicUiThemeSettings:
    defaultfg = "#000000"
    disabledfg = "#999999"
    frame = "#dcdad5"
    window = "#ffffff"
    dark = "#cfcdc8"
    darker = "#bab5ab"
    darkest = "#9e9a91"
    lighter = "#eeebe7"
    selectbg = "#4a6984"
    selectfg = "#ffffff"
    altindicator = "#5895bc"
    disabledaltindicator = "#a0a0a0"

    return {
        ".": {
            "configure": {
                "background": frame,
                "foreground": defaultfg,
                "bordercolor": darkest,
                "darkcolor": dark,
                "lightcolor": lighter,
                "troughcolor": darker,
                "selectbackground": selectbg,
                "selectforeground": selectfg,
                "selectborderwidth": 0,
                "font": "TkDefaultFont",
            },
            "map": {
                "background": [("disabled", frame), ("active", lighter)],
                "foreground": [("disabled", disabledfg)],
                "selectbackground": [("!focus", darkest)],
                "selectforeground": [("!focus", "white")],
            },
        },
        "TButton": {
            "configure": {
                "anchor": "center",
                "width": scale(11),
                "padding": scale(5),
                "relief": "raised",
            },
            "map": {
                "background": [("disabled", frame), ("pressed", darker), ("active", lighter)],
                "lightcolor": [("pressed", darker)],
                "darkcolor": [("pressed", darker)],
                "bordercolor": [("alternate", "#000000")],
            },
        },
        "Toolbutton": {
            "configure": {"anchor": "center", "padding": scale(2), "relief": "flat"},
            "map": {
                "relief": [
                    ("disabled", "flat"),
                    ("selected", "sunken"),
                    ("pressed", "sunken"),
                    ("active", "raised"),
                ],
                "background": [("disabled", frame), ("pressed", darker), ("active", lighter)],
                "lightcolor": [("pressed", darker)],
                "darkcolor": [("pressed", darker)],
            },
        },
        "TCheckbutton": {
            "configure": {
                "indicatorbackground": "#ffffff",
                "indicatormargin": [scale(1), scale(1), scale(6), scale(1)],
                "padding": scale(2),
            },
            "map": {
                "indicatorbackground": [
                    ("pressed", frame),
                    ("!disabled", "alternate", altindicator),
                    ("disabled", "alternate", disabledaltindicator),
                    ("disabled", frame),
                ]
            },
        },
        # TRadiobutton has same style as TCheckbutton
        "TRadiobutton": {
            "configure": {
                "indicatorbackground": "#ffffff",
                "indicatormargin": [scale(1), scale(1), scale(6), scale(1)],
                "padding": scale(2),
            },
            "map": {
                "indicatorbackground": [
                    ("pressed", frame),
                    ("!disabled", "alternate", altindicator),
                    ("disabled", "alternate", disabledaltindicator),
                    ("disabled", frame),
                ]
            },
        },
        "TMenubutton": {"configure": {"width": scale(11), "padding": scale(5), "relief": "raised"}},
        "TEntry": {
            "configure": {"padding": scale(1), "insertwidth": scale(1)},
            "map": {
                "background": [("readonly", frame)],
                "bordercolor": [("focus", selectbg)],
                "lightcolor": [("focus", "#6f9dc6")],
                "darkcolor": [("focus", "#6f9dc6")],
            },
        },
        "TCombobox": {
            "configure": {
                "padding": [scale(4), scale(2), scale(2), scale(2)],
                "insertwidth": scale(1),
            },
            "map": {
                "background": [("active", lighter), ("pressed", lighter)],
                "fieldbackground": [("readonly", "focus", selectbg), ("readonly", frame)],
                "foreground": [("readonly", "focus", selectfg)],
                "arrowcolor": [("disabled", disabledfg)],
            },
        },
        "ComboboxPopdownFrame": {"configure": {"relief": "solid", "borderwidth": scale(1)}},
        "TSpinbox": {
            "configure": {"arrowsize": scale(10), "padding": [scale(2), 0, scale(10), 0]},
            "map": {"background": [("readonly", frame)], "arrowcolor": [("disabled", disabledfg)]},
        },
        "TNotebook.Tab": {
            "configure": {"padding": [scale(6), scale(2), scale(6), scale(2)]},
            "map": {
                "padding": [("selected", [scale(6), scale(4), scale(6), scale(4)])],
                "background": [("selected", frame), ("", darker)],
                "lightcolor": [("selected", lighter), ("", dark)],
            },
        },
        "Treeview": {
            "configure": {"background": window},
            "map": {
                "background": [
                    ("disabled", frame),
                    ("!disabled", "!selected", window),
                    ("selected", selectbg),
                ],
                "foreground": [
                    ("disabled", disabledfg),
                    ("!disabled", "!selected", defaultfg),
                    ("selected", selectfg),
                ],
            },
        },
        # Treeview heading
        "Heading": {
            "configure": {
                "font": "TkHeadingFont",
                "relief": "raised",
                "padding": [scale(3), scale(3), scale(3), scale(3)],
            }
        },
        "TLabelframe": {"configure": {"labeloutside": True, "labelmargins": [0, 0, 0, scale(4)]}},
        "TProgressbar": {"configure": {"background": frame}},
        "Sash": {"configure": {"sashthickness": ems_to_pixels(0.6), "gripcount": 10}},
    }
'''











from typing import Callable, Dict, Union  # @UnusedImport
from thonny.misc_utils import running_on_linux, running_on_mac_os, running_on_windows
from thonny.ui_utils import ems_to_pixels
from thonny.workbench import BasicUiThemeSettings, CompoundUiThemeSettings


'''
def kyanite_ui() -> BasicUiThemeSettings:
    x = "#999999"
    return {
        ".": {
            "configure": {
                "foreground": x,
            },
    }
'''

def load_plugin() -> None:
    get_workbench().add_syntax_theme('Kyanite syntax', None, kyanite_syntax)
    #get_workbench().add_ui_theme('Kyanite ui', None, kyanite_ui)



