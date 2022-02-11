import os

from kivymd.app import MDApp

from root import Root


class MainApp(MDApp):
    volume = 1
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.root = Root()
        return self.root

    def on_start(self):
        self.root.push('main')


if __name__ == "__main__":
    MainApp().run()
