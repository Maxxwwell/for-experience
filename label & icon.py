from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon


class DemoApp(MDApp):
    def build(self):
        label = MDLabel(text="Hello world", halign="center", theme_text_color="Primary",
                        font_style="Body1")
        icon_label = MDIcon(icon="language-python", halign="center")
        return icon_label


DemoApp().run()
