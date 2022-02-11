import json
import os

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.screenmanager import ScreenManager


class Root(ScreenManager):
    screens_data = None
    screens_list = ListProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self._pop)
        with open('utils/pages.json') as f:
            self.screens_data = json.load(f)

    def push(self, screen_name, data=None, side="left", _from_pop=False):

        # checks that the screen already added to the screen-manager
        if not self.has_screen(screen_name):
            screen = self.screens_data[screen_name]
            # loads the kv file
            Builder.load_file(screen["kv_file"])
            # imports the screen class dynamically
            exec(screen["import"])
            # calls the screen class to get the instance of it
            screen_object = eval(screen["object"])
            # automatically sets the screen name using the arg that passed in set_current
            screen_object.name = screen_name
            # finally, adds the screen to the screen-manager
            self.add_widget(screen_object)

        # sets transition direction
        self.transition.direction = side
        # sets to the current screen
        self.current = screen_name
        # add screen to screen list
        if not _from_pop:
            self.screens_list.append({"name": screen_name, "side": side})
        # call on_pre_load method
        if data:
            self.get_screen(screen_name).on_push(data)

    def _pop(self, instance, key, *args):
        if key == 27:
            self.pop()
            return True

    def pop(self):

        if len(self.screens_list) > 1:
            prev_side = self.screens_list.pop()["side"]
            prev_screen = self.screens_list[-1]

            if prev_side == "left":
                side = "right"
            elif prev_side == "right":
                side = "left"
            elif prev_side == "up":
                side = "down"
            elif prev_side == "down":
                side = "up"
            self.push(prev_screen["name"], data=None, side=side, _from_pop=True)
