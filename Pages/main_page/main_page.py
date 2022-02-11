import random

from kivy.animation import Animation
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp

from utils.constants import db, db_sub, db_com, db_per, db_end, db_imp


class MainPage(Screen):
    card = ObjectProperty(None)
    add = ObjectProperty(None)
    pipup = ObjectProperty(None)
    swipeset = ObjectProperty(None)
    addition_score_input = ObjectProperty(None)
    addition_streak_input = ObjectProperty(None)
    addition_time_input = ObjectProperty(None)
    subtraction_score_input = ObjectProperty(None)
    subtraction_streak_input = ObjectProperty(None)
    subtraction_time_input = ObjectProperty(None)
    combined_score_input = ObjectProperty(None)
    combined_streak_input = ObjectProperty(None)
    combined_time_input = ObjectProperty(None)
    setting = ObjectProperty(None)
    back_image = ObjectProperty(None)
    monk_img = ObjectProperty(None)
    percent_text_input = ObjectProperty(None)
    no_of_games = ObjectProperty(None)
    update_button = ObjectProperty(None)
    checkbox_audio = ObjectProperty(None)
    percentage_score_input = ObjectProperty(None)
    percentage_streak_input = ObjectProperty(None)
    percentage_time_input = ObjectProperty(None)
    labelleele = ObjectProperty(None)
    main_label = ObjectProperty(None)
    card_two = ObjectProperty(None)
    rule_card = ObjectProperty(None)
    icon_1_text = ObjectProperty(None)
    icon_1 = ObjectProperty(None)
    timing_1_text = ObjectProperty(None)
    timing_1 = ObjectProperty(None)
    last_hint = ObjectProperty(None)
    the_swipe_button = ObjectProperty(None)
    mental = ObjectProperty(None)
    game_over = ObjectProperty(None)
    text1 = ObjectProperty(None)
    mdcard = ObjectProperty(None)

    unlock = False
    status = 'disable'

    def randomizer(self):
        lister = ["Hey, bud!", "Fellow warrior!", "Hello, Friend", "Heyya Champ!", "Little Grasshoppa!",
                  "M.V.P's here!"]
        a = random.choice(lister)
        self.main_label.text = a

    def popup_animate(self):
        anim = Animation(my_x_hint=0.53, opacity=1, duration=0.3)
        anim2 = Animation(opacity=0, duration=0.3)
        anim.start(self.pipup)
        anim2.start(self.swipeset)
        anim2.start(self.card)
        anim2.start(self.card_two)
        anim2.start(self.setting)
        anim2.start(self.mental)

    def popup_out(self):
        anim = Animation(my_x_hint=-0.5, opacity=1, duration=0.5)
        anim2 = Animation(opacity=1, duration=1)
        anim.start(self.pipup)
        anim2.start(self.swipeset)
        anim2.start(self.card)
        anim3 = Animation(opacity=1, duration=0.3)
        anim3.start(self.setting)
        anim3.start(self.card_two)
        anim2.start(self.mental)

    def rule_button(self):
        anim = Animation(the_x=0.5, the_y=0.4, duration=0.05)
        anim.start(self.rule_card)
        anim.bind(on_complete=self.rule_button_up)

    def rule_button_up(self, *args):
        anim = Animation(the_x=0.5, the_y=0.92, duration=0.5)
        self.the_swipe_button.disabled = True
        anim.start(self.rule_card)
        anim.bind(on_complete=self.the_rule_one)

    def the_rule_one(self, *args):
        anim = Animation(opacity=1, duration=0.8)
        anim.start(self.icon_1)
        anim.start(self.icon_1_text)
        anim.bind(on_complete=self.the_rule_two)

    def the_rule_two(self, *args):
        anim = Animation(opacity=1, duration=0.8)
        anim.start(self.timing_1)
        anim.start(self.timing_1_text)
        anim.bind(on_complete=self.the_rule_three)

    def the_rule_three(self, *args):
        anim = Animation(opacity=1, duration=1)
        anim.start(self.last_hint)

    def roll_back(self):
        self.the_swipe_button.disabled = False
        self.icon_1.opacity = 0
        self.icon_1_text.opacity = 0
        self.timing_1.opacity = 0
        self.timing_1_text.opacity = 0
        self.last_hint.opacity = 0
        self.rule_card.the_y = 0.5

    def AdditionInfo(self):
        score, streak, time = db.get_info()
        max_score = max(score)
        max_streak = max(streak)
        max_time = min(time)
        self.addition_score_input.text = str(max_score)
        self.addition_streak_input.text = str(max_streak)
        self.addition_time_input.text = str(max_time)

    def SubtractionInfo(self):
        score, streak, time = db_sub.get_info()
        max_score = max(score)
        max_streak = max(streak)
        max_time = min(time)
        self.subtraction_score_input.text = str(max_score)
        self.subtraction_streak_input.text = str(max_streak)
        self.subtraction_time_input.text = str(max_time)

    def CombinedInfo(self):
        score, streak, time = db_com.get_info()
        max_score = max(score)
        max_streak = max(streak)
        max_time = min(time)
        self.combined_score_input.text = str(max_score)
        self.combined_streak_input.text = str(max_streak)
        self.combined_time_input.text = str(max_time)

    def PercentInfo(self):
        score, streak, time = db_per.get_info()
        max_score = max(score)
        max_streak = max(streak)
        max_time = min(time)
        self.percentage_score_input.text = str(max_score)
        self.percentage_streak_input.text = str(max_streak)
        self.percentage_time_input.text = str(max_time)

    def ending_animation(self):
        anim3 = Animation(opacity=0, duration=0.5)
        anim1 = Animation(color=[1, 1, 1, 1], my_x=0.5, my_y=0.6, duration=2)
        anim2 = Animation(color=[1, 1, 1, 1], duration=2)
        anim3.start(self.text1)
        anim3.start(self.update_button)
        anim3.start(self.no_of_games)
        # anim3.start(self.percent_text_input)
        anim3.start(self.mdcard)
        anim1.start(self.monk_img)
        anim2.start(self.back_image)
        anim2.bind(on_complete=self.ending_followup)

    def ending_followup(self, *args):
        anim1 = Animation(my_x=0.5, my_y=0.25, duration=1)
        anim1.start(self.percent_text_input)
        anim1.bind(on_complete=self.ending_followup_sec)

    def ending_followup_sec(self, *args):
        anim1 = Animation(color=[0.7, 0.7, 0.7, 1], duration=2)
        anim1.start(self.monk_img)
        anim1.start(self.back_image)
        anim1.bind(on_complete=self.endd)

    def endd(self, *args):
        anim1 = Animation(opacity=1, duration=0.5)
        anim1.start(self.game_over)

    def ending(self):
        db_end.load()
        current_value, the_summation = db_imp.updatedCal()
        if current_value >= 0 and the_summation != False:
            self.no_of_games.opacity = 0
            if self.unlock is True:
                the_end_value = int(current_value) + int(the_summation)
                print("percent: ", the_end_value)
                if the_end_value < 100:
                    self.percent_text_input.text = (str(the_end_value) + "%")
                    db_end.rewrite(the_end_value)
                elif the_end_value >= 100:
                    self.percent_text_input.text = (str(100) + "%")
                    db_end.rewrite(100)
                self.unlock = False
                if self.percent_text_input.text == "100%":
                    self.ending_animation()
        else:
            self.update_button.disabled = True
            self.no_of_games.opacity = 1

    def off(self):
        anim = Animation(opacity=0, duration=0)
        anim.start(self.percent_text_input)

    def glow_up(self):
        anim = Animation(color=[1, 1, 1, 1], duration=2)
        anim.start(self.back_image)
        anim.start(self.monk_img)
        anim.bind(on_complete=self.glow_stay)

    def glow_stay(self, *args):
        anim = Animation(color=[1, 1, 1, 1], duration=0.5)
        anim.start(self.back_image)
        anim.start(self.monk_img)
        anim.bind(on_complete=self.glow_down)

    def glow_down(self, *args):
        anim = Animation(color=[50 / 255, 50 / 255, 50 / 255, 1], duration=0.4)
        anim.start(self.back_image)
        anim.start(self.monk_img)
        anim.bind(on_complete=self.love)

    def love(self, *args):
        anim = Animation(opacity=1, duration=0.5)
        anim.start(self.percent_text_input)

    def improv(self):
        anim = Animation(opacity=1, duration=3)
        anim.start(self.percent_text_input)

    def on_checkbox_active(self, checkbox, value):  # active: down, when clicked, value is True
        if value:  # inactive: normal value is False
            print(value)
            MDApp.get_running_app().volume = 1
        else:
            print(value)
            MDApp.get_running_app().volume = 0

    def button_anim(self):
        anim = Animation(size=(70, 70), duration=0.9)
        anim.start(self.setting)
        anim.bind(on_complete=self.followup)

    def followup(self, *args):
        anim = Animation(size=(60, 60), duration=0.9)
        anim.start(self.setting)

    def on_enter(self):
        self.randomizer()
        self.AdditionInfo()
        self.SubtractionInfo()
        self.CombinedInfo()
        self.PercentInfo()
        db_imp.load()
        add = (str(db_end.load()) + "%")
        self.percent_text_input.text = add
        if db_imp.val() is True:
            self.update_button.disabled = False
            self.no_of_games.opacity = 0
        else:
            self.update_button.disabled = True
            self.no_of_games.opacity = 1

    def on_pre_enter(self):
        self.roll_back()
