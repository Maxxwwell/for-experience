from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem

list_helper = """
Screen:
    ScrollView:
        MDList:
            id: container
            

"""


class ListApp(MDApp):

    def build(self):
        screen = Builder.load_string(list_helper)

        return screen

    def on_start(self):
        for i in range(20):
            items = OneLineListItem(text="item " + str(i))
            self.root.ids.container.add_widget(items)


ListApp().run()
