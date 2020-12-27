from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import Screen


class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        table = MDDataTable(column_data=[
            ("Food", dp(30))
        ])
        screen.add_widget(table)
        return screen


DemoApp().run()
