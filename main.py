from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.dropdown import DropDown
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout


class HomeScreen(Screen):
    pass


class NeedHelp(Screen):
    pass


class rohanCode(Screen):
    pass


class shashwatCode(Screen):
    pass


# class for functions
class ImageButton(ButtonBehavior, Image):
    pass


# then make a clickable grid
class GridButton(GridLayout, ButtonBehavior):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


GUI = Builder.load_file('main.kv')


class MainApp(App):
    def build(self):
        return GUI

    def change_screen(self, screen_name):
        global screen_manager
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current = screen_name


MainApp().run()
