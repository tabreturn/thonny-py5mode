# theme based on Processing 4.0b3 default theme, Kyanite

from thonny import get_workbench
from thonny.workbench import UiThemeSettings
from thonny.plugins.clean_ui_themes import clean


def load_plugin() -> None:
    get_workbench().add_ui_theme(
        "Kyanite UI",
        "Clean Sepia",
        clean(
            frame_background="#FF0000",
            text_background="#0000FF",
            normal_detail="#FFFF00",
            high_detail="#00FF00",
            low_detail="#00FFFF",
            normal_foreground="#660066",
            high_foreground="#006600",
            low_foreground="#000066",
            custom_menubar=0,
        ),
    )

    print('KYANITE UI LOADED .....................................')

