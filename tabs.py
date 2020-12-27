from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase


KV = """
BoxLayout:
    orientation: "vertical"
    MDToolbar:
        title: "Example Tabs"
    MDTabs:
        id: android_tabs
        on_tab_switch: app.on_tab_switch(*args)
<Tab>:
    
    MDLabel:
        id: label
        text: "first tab"
        halign: "center"
        
        
"""


class Tab(FloatLayout, MDTabsBase):
    pass


class DemoApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        for i in range(20):
            self.root.ids.android_tabs.add_widget(Tab(text=f"Tab {i}"))

    def on_tab_switch(
            self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        instance_tab.ids.label.text = tab_text


DemoApp().run()
