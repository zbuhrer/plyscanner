import flet as ft
# import json, requests


from flet import Page, Theme, ThemeVisualDensity, colors
from utils.extras import *
from ui.index import MainPage, Login, Settings, Chat
        

class App(ft.Page):
    def __init__(self,pg:ft.Page):
        pg.window_title_bar_buttons_hidden = True
        pg.window_frameless = True
        pg.window_width = base_width
        pg.window_height = base_height
        pg.window_min_width = base_width
        pg.window_min_height = base_height
        pg.window_max_width = base_width
        pg.window_max_height = base_height
        pg.window_resizable  = False
        pg.window_always_on_top = True
        # pg.window_opacity = 0.95
        
        
        
        self.chat_menu = ft.IconButton(icon=ft.icons.LOGIN, data='login', on_click=self.switch_page)
        self.login_menu = ft.IconButton(icon=ft.icons.CHAT_BUBBLE, data='chat', on_click=self.switch_page)
        self.settings_menu =ft.IconButton(icon=ft.icons.SETTINGS, data='settings', on_click=self.switch_page)

        pg.appbar = ft.AppBar(
            leading=ft.IconButton(ft.icons.HOME, data='main_page', on_click=self.switch_page),
            title=ft.Text("PlyScanner"),
            center_title=False,
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[self.login_menu,self.chat_menu,self.settings_menu])
                

        self.pg = pg
        self.main_page = MainPage(self.switch_page)
        self.login_page = Login(self.switch_page)
        self.settings_page = Settings(self.switch_page)
        self.chat_page = Chat(self.switch_page)
        
        self.screen_views = ft.Stack(
            expand=True,
            controls=[self.main_page])
        self.init_helper()
    
    def switch_page(self,e):
        if e.control.data == 'login':
            print("Loading Login Page")
            self.screen_views.controls.clear()
            self.screen_views.controls.append(self.login_page)
            self.screen_views.update()
            return     
        elif e.control.data == 'chat':
            print("Loading Chat Page")
            self.screen_views.controls.clear()
            self.screen_views.controls.append(self.chat_page)
            self.screen_views.update()
            return  
        elif e.control.data == 'settings':
            print("Loading Settings Page")
            self.screen_views.controls.clear()
            self.screen_views.controls.append(self.settings_page)
            self.screen_views.update()
            return
        elif e.control.data == 'main_page':
            print("Loading Main Page")
            self.screen_views.controls.clear()
            self.screen_views.controls.append(self.main_page)
            self.screen_views.update()
            return


    def init_helper(self):
        self.pg.add(self.screen_views)



ft.app(target=App,assets_dir="assets")