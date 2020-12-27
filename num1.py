from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.picker import MDDatePicker

screen_help = """
ScreenManager:
    WelcomeScreen:
    UsernameScreen:

<WelcomeScreen>
    name: "welcome"
    MDLabel:
        text: "Welcome"
        font_style: "H2"
        halign: "center"
        pos_hint: {"center_y": 0.6}
    MDFloatingActionButton: 
        icon: "language-python"
        user_font_size: "50sp"
        pos_hint: {"center_x": 0.5, "center_y": 0.4}
        size_hint_x: None
        on_press:
            root.manager.current = "username"
        
    
            

<UsernameScreen>
    name: "username"
    MDLabel:
        text: "I am username screen"
"""


class WelcomeScreen(Screen):
    pass


class UsernameScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(WelcomeScreen(name="welcome"))
sm.add_widget(UsernameScreen(name="username"))


class TestingApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_help)
        return screen


TestingApp().run()
