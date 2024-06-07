import flet as ft
import json, requests

from flet import Row, Column, Text, Container, FilePicker, canvas as cv
from flet import Stack, MainAxisAlignment, TextThemeStyle, View

class MainPage(ft.Container):
  def __init__(self,switch_page):
    super().__init__()
    # I know it feels a little backwards, but this is the right side of the page 
    # It will include controls for selecting and viewing the contents of a project directory 
    # in this context, the project directory is one which is full of media files that are 
    # being used for a pointcloud extraction 

      # file picker 
    self.selectafile = FilePicker()
    self.selectafile.allow_multiple = True
    self.selected_files = ft.Text("Selected Files")
    self.dirselect_button = ft.ElevatedButton("Select Project Directory", icon=ft.icons.FOLDER_OPEN, on_click=lambda _: self.selectafile.get_directory_path())
    self.source_dir_view = Container()

    # These are the left side of the page: controls for viewing the current pointcloud 
    # and the status of the current feature matching 

    self.ptc_btn = ft.FloatingActionButton(icon=ft.icons.SHAPE_LINE_SHARP)
    self.ptc_btn.on_click=self.show_pointcloud
    self.switch_page = switch_page
    self.render_view = Container(width=300, height=300, bgcolor="#333333")

    self.main_stack = Stack([
        Row([
            Column([
                self.ptc_btn,
                self.render_view]),
            Column([
                self.dirselect_button,
                self.selected_files
                ])])])
    self.content = self.main_stack
    self.init_helper()

  def pick_files_result(self, e: ft.FilePickerResultEvent):
        self.source_dir = e.path
        self.selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        )
        self.selected_files.update()
        print(f"Source dir: {self.source_dir}")
        return

  def show_pointcloud(self, e):
    print(f"Showing ptc data: {e}")
    self.render_view.clean()
    self.render_view.update()
    self.render_view.content = Text(value="Pointcloud data")
    self.ptc_btn.icon = ft.icons.SHAPE_LINE_OUTLINED
    self.ptc_btn.on_click = self.hide_pointcloud
    self.update()
    return
  
  def hide_pointcloud(self, e):
    print(f"Hiding ptc data: {e}")
    self.render_view.content = None
    self.render_view.update()
    self.ptc_btn.icon = ft.icons.SHAPE_LINE_SHARP
    self.ptc_btn.on_click = self.show_pointcloud
    self.update()
    return
  
  def init_helper(self):
    self.content=self.main_stack
    self.selectafile.on_result = self.pick_files_result
    self.update



    
class Login(ft.Container):
  def __init__(self,switch_page):
    super().__init__()
    self.switch_page = switch_page    
    self.content = ft.Column(
      controls=[
      ft.Text(value="Login Page")
      ])
    
class Settings(ft.Container):
  def __init__(self,switch_page):
    super().__init__()
    self.switch_page = switch_page    
    self.content = ft.Column(
      controls=[
      ft.Text(value="Settings Page confirmed working!")
      ])
    
class Chat(ft.Container):
  def __init__(self,switch_page):
    super().__init__()
    self.switch_page = switch_page    
    self.content = ft.Column(
      controls=[
      ft.Text(value="Chat Page confirmed working!")
      ])
    
