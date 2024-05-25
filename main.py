import flet
from flet import Page, Stack, UserControl, Container, Column, Row
from flet import Text, IconButton, WebView

from ui.ui import PlyScanner
from utils.extras import *


class App(Page):
    def __init__(self,pg:Page):
        # pg.window_title_bar_buttons_hidden = True
        # pg.window_frameless = True
        # pg.window_width = base_width
        # pg.window_height = base_height
        # pg.horizontal_alignment = flet.CrossAxisAlignment.CENTER
        # pg.vertical_alignment = flet.MainAxisAlignment.CENTER
        
        plyScanner = Stack(
                expand=True,
                controls=[
                    Row(expand=True, 
                        controls=[
                            Column(expand=True, controls=
                                    [Row([Text("A")]),Row([Text("B")])]),
                            Column(expand=True, controls=
                                    [Row([Text("C")]),Row([Text("D")])])])])
        
        pg.add(plyScanner)



if __name__ == "__main__":
    flet.app(target=App)
