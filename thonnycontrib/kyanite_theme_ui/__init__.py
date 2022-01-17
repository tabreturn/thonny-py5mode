'''kyanite ui theme
   theme inspired by processing 4.0b3 default theme, kyanite
'''

from thonny import get_workbench
from thonny.plugins.clean_ui_themes import clean


def load_plugin() -> None:
    get_workbench().add_ui_theme(
      'Kyanite UI',
      'Clean Sepia',
      clean(
        frame_background='#6BA0C7',
        text_background='#FFFFF2',
        normal_detail='#C4E9FF',
        high_detail='#B4D9EF',
        low_detail='#A4C9DF',
        normal_foreground='#002233',
        high_foreground='#002233',
        low_foreground='#000066',
        custom_menubar=0,
      ),
    )
