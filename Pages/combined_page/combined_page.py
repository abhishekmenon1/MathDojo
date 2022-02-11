from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.metrics import sp, dp
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
import random
from random import randint

from kivymd.app import MDApp

from utils.constants import  db_imp, db_com


class CombinedPage(Screen):
    operating = ["+", "-", "+", "-"]
    timer_1 = 0  # Introducing variables, lists, ObjectProperties
    timer_2 = 0
    timer_3 = 0
    timer_4 = 0
    sign_ch = ""
    total_question = 0
    right_answers = 0
    list = []
    ttop = []
    bbot = []
    user_ans = []
    real_ans = []
    fire_list = []
    joined_eq = []
    a_the_streak = 0
    alpha = 0
    ctdown = 64  # for the visible countdown timer
    ctdown2 = 65  # for the countdown whe the "result score" popup box shows up
    streak = 0  # counts the streak
    thescore = 0  # the score of the player
    count = 4  # the 3,2,1, GO! timer
    button_check = False
    topnum = 0
    botnum = 0
    tim = 0
    time = ObjectProperty(None)
    answer = ObjectProperty(None)
    top_num = ObjectProperty(None)
    bot_num = ObjectProperty(None)
    correct = ObjectProperty(None)
    operator = ObjectProperty(None)
    next = ObjectProperty(None)
    score = ObjectProperty(None)
    clock = ObjectProperty(None)
    clock_name = ObjectProperty(None)
    popup = ObjectProperty(None)
    final_score = ObjectProperty(None)
    equations = ObjectProperty(None)
    percentage = ObjectProperty(None)
    attempts = ObjectProperty(None)
    the_seconds = ObjectProperty(None)
    aq = ObjectProperty(None)
    no_ques = ObjectProperty(None)
    time_label = ObjectProperty(None)
    thescore_label = ObjectProperty(None)
    no_ques2 = ObjectProperty(None)
    go_home = ObjectProperty(None)
    img = ObjectProperty(None)
    hero = ObjectProperty(None)
    one = ObjectProperty(None)
    two = ObjectProperty(None)
    three = ObjectProperty(None)
    ans = ObjectProperty(None)
    grid = ObjectProperty(None)
    streaknum = ObjectProperty(None)
    streakcomment = ObjectProperty(None)
    end_streak = ObjectProperty(None)
    xae = ObjectProperty(None)
    back_card = ObjectProperty(None)
    top_card = ObjectProperty(None)
    backspace = ObjectProperty(None)
    back_card2 = ObjectProperty(None)
    back_card3 = ObjectProperty(None)
    progressbar = ObjectProperty(None)
    test_label = ObjectProperty(None)
    visual = ObjectProperty(None)
    scroller = ObjectProperty(None)
    question_answer = ObjectProperty(None)
    question_part = ObjectProperty(None)
    answer_part = ObjectProperty(None)
    realanswer_part = ObjectProperty(None)
    swipeup = ObjectProperty(None)
    swipeupicon = ObjectProperty(None)
    samurai = ObjectProperty(None)
    samurai_two = ObjectProperty(None)
    what = ObjectProperty(None)
    final_score_label = ObjectProperty(None)
    the_seconds_new = ObjectProperty(None)
    visual_depression = ObjectProperty(None)
    img_final = ObjectProperty(None)

    def five_Second_end(self):
        anim = Animation(opacity=0.5, duration=0.3)
        anim.start(self.img_final)
        anim.bind(on_complete=self.the_next_thing)

    def the_next_thing(self, *args):
        anim = Animation(opacity=0, duration=0.3)
        anim.start(self.img_final)

    def popup_animate(self):
        anim = Animation(my_x_hint=0.53, opacity=1, duration=0.3)
        anim.start(self.popup)
        anim.bind(on_complete=self.mycallback)

    def mycallback(self, *args):
        anim = Animation(my_x_hint=0.5, duration=0.1)
        anim.start(self.popup)

    def numpad_one(self):  # for the number pad numbers
        a = "1"
        self.sum(a)

    def numpad_two(self):
        a = "2"
        self.sum(a)

    def numpad_three(self):
        a = "3"
        self.sum(a)

    def numpad_four(self):
        a = "4"
        self.sum(a)

    def numpad_five(self):
        a = "5"
        self.sum(a)

    def numpad_six(self):
        a = "6"
        self.sum(a)

    def numpad_seven(self):
        a = "7"
        self.sum(a)

    def numpad_eight(self):
        a = "8"
        self.sum(a)

    def numpad_nine(self):
        a = "9"
        self.sum(a)

    def numpad_zero(self):
        a = "0"
        self.sum(a)

    def sum(self, num):  # takes the values of the number pad methods and joins them together
        self.list.append(num)
        self.answer.text = (''.join(self.list))

    def fadein_img(self):  # animation for the background image
        fadein = Animation(opacity=0.5, duration=4.5)
        fadein.start(self.img)

    def scorean_card(self):
        colorcard = Animation(line_color=(0, 1, 0, 1), duration=0.3)
        colorcard.start(self.back_card)
        colorcard.start(self.back_card2)
        colorcard.start(self.back_card3)
        colorcard.bind(on_complete=self.scorean_switch)

    def scorean_switch(self, *args):
        switch2 = Animation(line_color=(255 / 255, 214 / 255, 202 / 255, 1), duration=0.5)
        switch2.start(self.back_card)
        switch2.start(self.back_card2)
        switch2.start(self.back_card3)

    def scorered_card(self):
        colorcard = Animation(line_color=(1, 0, 0, 1), duration=0.3)
        colorcard.start(self.back_card)
        colorcard.start(self.back_card2)
        colorcard.start(self.back_card3)
        colorcard.bind(on_complete=self.scoreanred_switch)

    def scoreanred_switch(self, *args):
        switch2 = Animation(line_color=(255 / 255, 214 / 255, 202 / 255, 1), duration=0.5)
        switch2.start(self.back_card)
        switch2.start(self.back_card2)
        switch2.start(self.back_card3)

    def ann(self, widget, *args):  # method for animating popup box
        anim = Animation(opacity=1)
        anim.start(widget)

    def enterin(self):  # method for animating the streak
        color = Animation(opacity=1, duration=0.05)
        color.start(self.correct)

    def motivation(self):
        list = ['assets/images/ko.png', 'assets/images/monk.png', 'assets/images/ok.png', 'assets/images/easy.png', 'assets/images/firec.png',
                'assets/images/good.png', 'assets/images/woah.png', 'assets/images/yes.png']
        a = random.choice(list)
        self.visual.source = a
        self.expandingb()

    def expandingb(self):
        self.next.disabled = True
        self.visual.size = (0, 0)
        self.visual.opacity = 1
        val = Animation(opacity=0, value=100, duration=0.1)
        opac = Animation(opacity=0, duration=0.1)
        anim = Animation(size=(dp(1280 / 1.4), dp(720 / 1.4)), duration=0.15)
        opac.start(self.top_num)
        opac.start(self.bot_num)
        opac.start(self.operator)
        val.start(self.progressbar)
        anim.start(self.visual)
        anim.bind(on_complete=self.expand2)

    def expand2(self, *args):
        anim = Animation(size=(dp(1280 / 4.5), dp(720 / 4.5)), duration=0.1)
        anim.start(self.visual)
        anim.bind(on_complete=self.expand3)

    def expand3(self, *args):
        anim = Animation(opacity=0, duration=0.4)
        anim.start(self.visual)
        anim.bind(on_complete=self.expand4)

    def expand4(self, *args):
        self.progressbar.value = 100
        self.clear()
        self.next.disabled = False
        anim2 = Animation(opacity=1, duration=0.1)
        anim2.start(self.top_num)
        anim2.start(self.bot_num)
        anim2.start(self.operator)
        anim2.start(self.progressbar)

    def depression(self):
        list = ['assets/images/no1.png', 'assets/images/no2.png', 'assets/images/no3.png', 'assets/images/no4.png', 'assets/images/no5.png']
        a = random.choice(list)
        self.visual_depression.source = a
        self.expandingc()

    def expandingc(self):
        # self.visual.size = (0, 0)
        self.next.disabled = True
        self.visual_depression.opacity = 0
        val = Animation(opacity=0, value=100, duration=0.1)
        opac = Animation(opacity=0, duration=0.1)
        anim = Animation(opacity=1, duration=0.15)
        opac.start(self.top_num)
        opac.start(self.bot_num)
        opac.start(self.operator)
        val.start(self.progressbar)
        anim.start(self.visual_depression)
        anim.bind(on_complete=self.expand2c)

    def expand2c(self, *args):
        anim = Animation(opacity=1, duration=0.2)
        anim.start(self.visual_depression)
        anim.bind(on_complete=self.expand3c)

    def expand3c(self, *args):
        self.next.disabled = False
        anim = Animation(opacity=0, duration=0.4)
        anim.start(self.visual_depression)
        anim.bind(on_complete=self.expand4c)

    def expand4c(self, *args):
        self.progressbar.value = 100
        self.next.disabled = False
        self.clear()
        anim2 = Animation(opacity=1, duration=0.1)
        anim2.start(self.top_num)
        anim2.start(self.bot_num)
        anim2.start(self.operator)
        anim2.start(self.progressbar)

    def animations_roll(self):
        rise = Animation(opacity=1, duration=0.3)
        rise.start(self.top_card)
        rise.start(self.scolbl)
        rise.start(self.score)
        rise.bind(on_complete=self.partial_set)

    def end_music(self, value, name):  # end soundclip when game ends
        music = SoundLoader.load(name)
        if music:
            music.play()
            new_val = value - 0.2
            if new_val < 0:
                music.volume = 0
            else:
                music.volume = new_val
        else:
            pass

    def right_music(self, value):  # end soundclip when game ends
        sounds = ["assets/audio/ok.wav", "assets/audio/Yes.wav", "assets/audio/right.wav"]
        a = random.choice(sounds)
        music = SoundLoader.load(a)
        if music:
            music.play()
            music.volume = value
        else:
            pass

    def partial_set(self, *args):
        rise = Animation(opacity=1, duration=0.5)
        rise.start(self.test_label)
        rise.bind(on_complete=self.next_set)

    def next_set(self, *args):
        anim = Animation(opacity=1, duration=0.4)
        anim.start(self.answer)
        anim.start(self.next)
        anim.bind(on_complete=self.partial_set2)

    def partial_set2(self, *args):
        rise = Animation(opacity=1, duration=0.5)
        rise.start(self.test_label)
        rise.bind(on_complete=self.next_set2)

    def next_set2(self, *args):
        anim = Animation(opacity=1, duration=0.4)
        anim.start(self.grid)
        anim.start(self.backspace)
        anim.bind(on_complete=self.partial_set3)

    def partial_set3(self, *args):
        twofade = Animation(opacity=1, value=99, duration=2)
        #        secfade = Animation(line_color=[248/255, 181/255, 12/255, 1], md_bg_color=[0, 0, 0, 0.4], duration=0.5)
        secfade = Animation(line_color=[255 / 255, 214 / 255, 202 / 255, 1], md_bg_color=[0, 0, 0, 0.4], duration=0.5)
        secfade2 = Animation(line_color=[255 / 255, 214 / 255, 202 / 255, 1], duration=2)
        #        secfade2 = Animation(line_color=[248/255, 181/255, 12/255, 1],  duration=2)
        secfade.start(self.back_card)
        secfade2.start(self.back_card2)
        secfade2.start(self.back_card3)
        twofade.start(self.progressbar)
        secfade2.bind(on_complete=self.next_set4)

    def next_set4(self, *args):
        infade = Animation(opacity=1, duration=0.5)

        infade.start(self.top_num)
        infade.start(self.bot_num)
        infade.start(self.operator)
        infade.start(self.clock)
        infade.start(self.xae)

    def animate(self, timer):  # method for animating timer
        anim = Animation(opacity=0, duration=timer)
        anim.start(self.time)

    def expand(self, timer):  # method for animating label
        size = self.time.font_size
        expand = Animation(font_size=sp(size * 50), opacity=0, duration=timer)
        expand.start(self.time)

    def background_box_questiontimer(self, *args):
        infade = Animation(opacity=1, duration=0.5)
        infade.start(self.progressbar)

    def scorean(self, number):  # method for animating label
        self.thescore = self.thescore + number
        self.score.text = str(self.thescore)
        color = Animation(bold=True, color=(0, 1, 0, 1), duration=0.3)
        color.start(self.score)
        color.bind(on_complete=self.switchback)
        a = self.thescore
        return a

    def scorered(self):  # method for animating label
        color = Animation(color=(1, 0, 0, 1), duration=0.1)
        color.start(self.score)
        color.bind(on_complete=self.switchback)

    def switchback(self, *args):  # method for animating label
        switch = Animation(bold=False, color=(1, 1, 1, 1), duration=0.5)
        switch.start(self.score)

    def streakcounter(self):  # method to show the streak number and the "fire" during the game
        self.streak = self.streak + 1
        if self.streak >= 3:
            self.enterin()
            self.correct.color = (0, 1, 1, 1)
            self.stfire(self.streak)
            st = str(self.streak)
            self.correct.text = ("x" + st)

    def countdown(self, *args):  # countdown before the game starts (eg. 3,2,1 GO!)
        self.count = self.count - 1
        if self.count > 0:
            self.time.opacity = 1
            self.time.text = str(self.count)
            self.animate(1)
            if self.count == 1:
                listy = ["assets/audio/ready_1.wav", "assets/audio/ready_2.wav", "assets/audio/ready_3.wav"]
                rando = random.choice(listy)
                self.end_music(MDApp.get_running_app().volume, rando)
        elif self.count == 0:
            self.time.opacity = 1
            self.time.text = "GO!"
            listyy = ["assets/audio/fight_1.wav", "assets/audio/fight_2.wav", "assets/audio/fight_3.wav"]
            randoo = random.choice(listyy)
            self.end_music(MDApp.get_running_app().volume, randoo)
            self.time.font_size = 10
            self.expand(0.8)
        else:
            self.time.text = ''

    def check(self):
        self.button_check = True
        return self.button_check

    def top_nd_bot(self, top, bot, userans, realans, sign):
        self.ttop.append(top)
        self.bbot.append(bot)
        self.user_ans.append(userans)
        self.real_ans.append(realans)

        for value, i in enumerate(self.ttop):
            first_num = i
            for value_two, j in enumerate(self.bbot):
                second_num = j
                if value == value_two:
                    continue
        if sign == "-":
            joined = first_num, " - ", second_num
            self.joined_eq.append(''.join(joined))
        elif sign == "+":
            joined = first_num, " + ", second_num
            self.joined_eq.append(''.join(joined))

    def grid_Values(self):
        if self.top_num.text != "" and self.bot_num.text != "":
            # del self.joined_eq[0]
            # del self.real_ans[0]
            # del self.user_ans[0]
            print("joined_eq: ", self.joined_eq)
            print("real: ", self.real_ans)
            print("users: ", self.user_ans)

            for value, i in enumerate(self.joined_eq):
                layout = self.question_part
                label1 = Label(text=i, bold=True)
                layout.add_widget(label1)

            for value, j in enumerate(self.user_ans):
                layout = self.answer_part
                label1 = Label(text=j)
                layout.add_widget(label1)

            for value, k in enumerate(self.real_ans):
                layout = self.realanswer_part
                label1 = Label(text=str(k))
                layout.add_widget(label1)
        else:
            pass

    def numberfamo(self):
        anim = Animation(opacity=1, duration=0.1)
        anim.start(self.what)
        anim.bind(on_complete=self.endisnear)

    def endisnear(self, *args):
        anim = Animation(opacity=1, duration=0.4)
        anim.start(self.what)
        anim.bind(on_complete=self.bbye)

    def bbye(self, *args):
        anim = Animation(opacity=0, duration=0.2)
        anim.start(self.what)

    def combine(self):  # method for the addition game, to get random numbers
        self.progressbar.value = 100
        self.answer.focus = True
        self.correct.text = ""
        if self.top_num.text != "" and self.bot_num.text != "":
            if self.answer.text != "":
                apple = self.answer.text.isdigit()
                if apple is True:
                    if self.operator.text == "+":
                        self.alpha = int(self.top_num.text) + int(self.bot_num.text)
                        sum = int(self.top_num.text) + int(self.bot_num.text)
                        if sum == int(self.answer.text) and self.button_check is True:
                            self.button_check = False
                            self.right_answers = self.right_answers + 1
                            self.motivation()
                            self.right_music(MDApp.get_running_app().volume)
                            self.total_question = self.total_question + 1
                            self.scorean_card()
                            self.streakcounter()
                            if self.streak < 2:
                                self.scorean(1)
                            elif 2 <= self.streak < 5:
                                self.scorean(2)
                            elif 5 <= self.streak < 9:
                                self.scorean(4)
                            elif 9 <= self.streak < 15:
                                self.scorean(5)

                        # else:
                        if sum != int(self.answer.text) and self.button_check is True:
                            self.streak = 0
                            self.depression()
                            sign_ch = '+'
                            self.top_nd_bot(self.top_num.text, self.bot_num.text, self.answer.text, sum, sign_ch)
                            self.total_question = self.total_question + 1
                            self.scorered()
                            self.scorered_card()

                    elif self.operator.text == "-":
                        self.alpha = int(self.top_num.text) - int(self.bot_num.text)
                        sub = int(self.top_num.text) - int(self.bot_num.text)
                        if sub == int(self.answer.text) and self.button_check is True:
                            self.button_check = False
                            self.right_answers = self.right_answers + 1
                            self.motivation()
                            self.right_music(MDApp.get_running_app().volume)
                            self.total_question = self.total_question + 1
                            self.scorean_card()
                            self.streakcounter()
                            if self.streak < 2:
                                self.scorean(1)
                            elif 2 <= self.streak < 5:
                                self.scorean(2)
                            elif 5 <= self.streak < 9:
                                self.scorean(4)
                            elif 9 <= self.streak < 15:
                                self.scorean(5)

                        # else:
                        if sub != int(self.answer.text) and self.button_check is True:
                            self.streak = 0
                            self.depression()
                            sign_ch = "-"
                            self.top_nd_bot(self.top_num.text, self.bot_num.text, self.answer.text, sub, sign_ch)
                            self.total_question = self.total_question + 1
                            self.scorered()
                            self.scorered_card()
                else:
                    self.streak = 0
                    self.depression()
                    self.total_question = self.total_question + 1
                    if self.operator.text == "+":
                        self.recko = int(self.top_num.text) + int(self.bot_num.text)
                    elif self.operator.text == "-":
                        self.recko = int(self.top_num.text) - int(self.bot_num.text)
                    self.top_nd_bot(self.top_num.text, self.bot_num.text, "non-number", self.recko, self.operator.text)
                    self.what.text = "What?"
                    self.numberfamo()
                    self.scorered()
                    self.scorered_card()

            else:
                self.depression()
                if self.operator.text == "+":
                    equation = self.topnum + self.botum
                    self.top_nd_bot(self.top_num.text, self.bot_num.text, "-", equation, self.operator.text)
                elif self.operator.text == "-":
                    equation = self.topnum - self.botum
                    self.top_nd_bot(self.top_num.text, self.bot_num.text, "-", equation, self.operator.text)

            self.combo_works()

        else:
            self.combo_works()

    def combo_works(self):
        self.operator.text = random.choice(self.operating)
        self.operator.color = (248 / 255, 181 / 255, 12 / 255, 1)
        self.operator.bold = True
        if self.streak < 2:
            i = randint(12, 25)
            self.top_num.text = str(i)
            j = randint(2, 11)
            self.bot_num.text = str(j)
            self.topnum = i
            self.botum = j

        elif 2 <= self.streak < 4:
            i = randint(35, 50)
            self.top_num.text = str(i)
            j = randint(16, 34)
            self.bot_num.text = str(j)
            self.topnum = i
            self.botum = j

        elif 4 <= self.streak < 7:
            i = randint(60, 80)
            self.top_num.text = str(i)
            j = randint(30, 59)
            self.bot_num.text = str(j)
            self.topnum = i
            self.botum = j

        elif 7 <= self.streak < 9:
            i = randint(91, 125)
            self.top_num.text = str(i)
            j = randint(50, 90)
            self.bot_num.text = str(j)
            self.topnum = i
            self.botum = j

        elif 9 <= self.streak < 15:
            i = randint(140, 190)
            self.top_num.text = str(i)
            j = randint(101, 139)
            self.bot_num.text = str(j)
            self.topnum = i
            self.botum = j

        elif self.streak >= 15:
            i = randint(220, 330)
            self.top_num.text = str(i)
            j = randint(160, 219)
            self.bot_num.text = str(j)
            self.topnum = i
            self.botum = j

    def removele(self):  # method to join the numbers pressed from the number pad
        self.list = self.list[:-1]
        self.answer.text = (''.join(self.list))

    def clear(self):
        self.list = []
        self.answer.text = ''

    def clkwork(self, *args):  # method for the game timer (starts at 60seconds, ends at 0secs)
        self.ctdown = self.ctdown - 1
        if self.ctdown >= 0:  # should be 0
            if self.ctdown <= 5:
                if self.ctdown == 4:
                    self.five_Second_end()
                    self.end_music(MDApp.get_running_app().volume, "assets/audio/end_five.wav")
                if self.ctdown == 3:
                    self.five_Second_end()
                    self.end_music(MDApp.get_running_app().volume, "assets/audio/end_five.wav")
                if self.ctdown == 2:
                    self.five_Second_end()
                    self.end_music(MDApp.get_running_app().volume, "assets/audio/end_five.wav")
                if self.ctdown == 1:
                    self.five_Second_end()
                    self.end_music(MDApp.get_running_app().volume, "assets/audio/last end five.wav")
                self.clock.color = self.clock_name.color = (1, 0, 0, 1)
                self.clock.font_size = 28
                self.clock.text = str(self.ctdown)
            else:
                self.clock.text = str(self.ctdown)
        else:
            self.clock.opacity = 0
            self.clock_name.opacity = 0

    def seconds_anim(self):
        anim = Animation(opacity=0, duration=0.5)
        anim.start(self.the_seconds_new)
        anim.bind(on_complete=self.seconds_anim_one)

    def seconds_anim_one(self, *args):
        anim = Animation(opacity=1, duration=1.8)
        anim.start(self.the_seconds_new)
        anim.bind(on_complete=self.seconds_anim_inter)

    def seconds_anim_inter(self, *args):
        anim = Animation(opacity=1, duration=0.9)
        anim.start(self.the_seconds_new)
        anim.bind(on_complete=self.seconds_anim_next)

    def seconds_anim_next(self, *args):
        anim = Animation(opacity=0, duration=0.4)
        anim.start(self.the_seconds_new)
        anim.bind(on_complete=self.seconds_anim_next_next)

    def seconds_anim_next_next(self, *args):
        anim = Animation(opacity=1, duration=0.3)
        anim.start(self.the_seconds)

    def seconds_anim_streak(self):
        anim = Animation(opacity=0, duration=2.5)
        # anim2 = Animation(opacity=0)
        # anim2.start(self.streaknum)
        anim.start(self.streak_label)
        anim.bind(on_complete=self.seconds_anim_streak_one)

    def seconds_anim_streak_one(self, *args):
        anim = Animation(opacity=1, duration=1.4)
        anim.start(self.streak_label)
        anim.bind(on_complete=self.seconds_anim_inter_streak)

    def seconds_anim_inter_streak(self, *args):
        anim = Animation(opacity=1, duration=1.7)
        anim.start(self.streak_label)
        anim.bind(on_complete=self.seconds_anim_next_streak)

    def seconds_anim_next_streak(self, *args):
        anim = Animation(opacity=0, duration=0.4)
        anim.start(self.streak_label)
        anim.bind(on_complete=self.seconds_anim_next_next_streak)

    def seconds_anim_next_next_streak(self, *args):
        anim = Animation(opacity=1, duration=0.3)
        anim.start(self.streaknum)

    def score_anim(self):
        anim = Animation(opacity=0, duration=0.5)
        anim.start(self.final_score_label)
        anim.bind(on_complete=self.score_anim_one)

    def score_anim_one(self, *args):
        anim = Animation(opacity=1, duration=1.4)
        anim.start(self.final_score_label)
        anim.bind(on_complete=self.score_anim_inter)

    def score_anim_inter(self, *args):
        anim = Animation(opacity=1, duration=0.5)
        anim.start(self.final_score_label)
        anim.bind(on_complete=self.score_anim_next)

    def score_anim_next(self, *args):
        anim = Animation(opacity=0, duration=0.4)
        anim.start(self.final_score_label)
        anim.bind(on_complete=self.score_anim_next_next)

    def score_anim_next_next(self, *args):
        anim = Animation(opacity=1, duration=0.3, color=(0, 1, 0, 1))
        anim.start(self.ids.final_score)

    def percent(self):  # method to add information on popup screen, percentage, time taken
        if self.total_question > 0:
            percent = int(self.right_answers / self.total_question * 100)
            self.tim = round((59.99 / self.total_question), 2)
            attemps = str(self.total_question)
            str_percent = str(percent)
            self.percentage.text = (str_percent + "%")
            self.attempts.text = attemps
            if db_imp.new_combine_ans(self.tim):
                self.seconds_anim()
                self.the_seconds.color = [0, 1, 0, 1]
                self.the_seconds.text = str(self.tim)
            else:
                self.the_seconds.opacity = 1
                self.the_seconds.text = str(self.tim)

            if percent == 100:
                self.percentage.color = (0, 1, 0, 1)
                self.scroller.disabled = True
                self.swipeup.opacity = 0
                self.swipeupicon.opacity = 0
                self.samurai_two.color = (0, 1, 0, 1)
                self.samurai_two.text = "100%, woah!"
                self.samurai.opacity = 0

            elif 80 <= percent < 100:
                self.percentage.color = (1, 1, 0, 1)

            elif 50 <= percent < 80:
                self.percentage.color = (250 / 255, 194 / 255, 0, 1)

            elif 30 <= percent < 49:
                self.percentage.color = (160 / 255, 44 / 255, 0, 1)

            else:
                self.percentage.color = (255 / 255, 0 / 255, 0, 1)

        else:
            return -1

    def stfire(self, fire):  # method to show the highest streak the player had in the popup box
        self.fire_list.append(fire)
        self.a_the_streak = max(self.fire_list)

        if 3 <= self.a_the_streak < 5:
            self.streaknum.text = str(max(self.fire_list))
            comp_one = ["Let's better that streak,[i] now![/i]", "Keep Practicing, Keep Improving.", "Good start.",
                        "Tough mind-workout,[i] eh?[/i]", "Get back at it,[i] champ[/i]."]
            self.samurai.text = random.choice(comp_one)
            self.samurai.color = (164 / 255, 103 / 255, 7 / 255, 1)

        elif 5 <= self.a_the_streak < 10:
            self.streaknum.text = str(max(self.fire_list))
            self.streaknum.color = (248 / 255, 181 / 255, 12 / 255, 1)
            compliments = ["Keep Trying,[i] Keep Winning.[/i]", "Keep at it, [i]champ![/i]",
                           "Keep at it, [i]champ![/i]", "Good Effort, [i]fellow warrior[/i]",
                           "You're getting there!"]
            self.samurai.text = random.choice(compliments)
            self.samurai.color = (129 / 255, 154 / 255, 14 / 255, 1)

        elif 10 <= self.a_the_streak < 15:
            self.streaknum.text = str(max(self.fire_list))
            self.streaknum.color = (5 / 255, 181 / 255, 12 / 255, 1)
            compliments = ["Now, lets cross [i]Streak-15[/i]", "Almost there,[i] buddy![/i]",
                           "You have [i]huuugee[/i] potential!", "Good Effort, [i]fellow warrior[/i]",
                           "You're getting there!", "Math Wiz in the making!"]
            self.samurai.text = random.choice(compliments)
            self.samurai.color = (16 / 255, 188 / 255, 235 / 255, 1)

        elif self.a_the_streak >= 15:
            self.streaknum.text = str(max(self.fire_list))
            self.streaknum.color = (5 / 255, 181 / 255, 12 / 255, 1)
            compliments_one = ["Wooah 100%,[i] NICE![/i]", "Holy,[i] MASTER![/i]", "Warrior turned, [i]LEADER[/i]",
                               "Good Job [b][i]Samurai[/i][/b]!", "BRUH, you might just become the next [i]sensei[/i]"]
            self.samurai_two.text = random.choice(compliments_one)
            self.samurai.color = (94 / 255, 217 / 255, 22 / 255, 1)

        else:
            self.streaknum.text = "--"

    def openpopup(self):  # method is called when the person decides to quit mid-way
        self.popupbox(True)

    def popupboxinfo(self):  # method for what the score popup box will show
        Clock.unschedule(self.countdown)
        Clock.unschedule(self.clkwork)
        Clock.unschedule(self.popupbox)
        Clock.unschedule(self.question_timer)
        self.popup_animate()
        # self.end_music(MDApp.get_running_app().volume)
        self.progressbar.opacity = 0
        self.clock_name.opacity = 0
        self.clock.opacity = 0
        self.top_card.opacity = 0
        self.xae.opacity = 0
        self.grid.opacity = 0
        self.grid.disabled = True
        self.scolbl.opacity = 0
        self.next.disabled = True
        self.scorechange()
        self.score.opacity = 0
        self.operator.opacity = 0
        self.answer.opacity = 0
        self.next.opacity = 0
        self.correct.opacity = 0
        self.back_card.line_color = (248 / 255, 181 / 255, 12 / 255, 0)
        self.back_card.md_bg_color = (0, 0, 0, 0)
        self.back_card2.line_color = (248 / 255, 181 / 255, 12 / 255, 0)
        self.back_card2.md_bg_color = (0, 0, 0, 0)
        self.back_card3.line_color = (248 / 255, 181 / 255, 12 / 255, 0)
        self.back_card3.md_bg_color = (0, 0, 0, 0)
        self.xae.disabled = True
        self.backspace.opacity = 0
        self.scroller.disabled = False
        self.back_card.opacity = 0
        self.back_card2.opacity = 0
        self.back_card3.opacity = 0

    def quit_popup(self):
        self.popupboxinfo()
        self.scroller.disabled = True
        self.end_music(MDApp.get_running_app().volume, "assets/audio/time_up.wav")
        self.no_ques2.opacity = self.no_ques.opacity = 1
        self.no_ques.italic = True
        self.time_label.opacity = 0
        self.the_seconds.text = ""
        self.aq.opacity = 0
        self.attempts.text = ""
        self.end_streak.opacity = 0
        self.streaknum.opacity = 0
        self.samurai.opacity = 0
        self.ids.final_score.text = "00"
        self.progressbar.opacity = 0
        self.thescore_label.opacity = 0
        self.percentage.opacity = 0
        self.backspace.opacity = 0
        self.swipeupicon.opacity = 0
        self.swipeup.opacity = 0

    def popupbox(self, hel):  # method to add popup screen
        self.ctdown2 = self.ctdown2 - 1
        hello = hel
        if self.ctdown2 == 0:  # at this time the popup box will open up
            self.popupboxinfo()
            self.percent()
            self.grid_Values()
            self.end_music(MDApp.get_running_app().volume, "assets/audio/gong.wav")
            if self.a_the_streak > 0:  # CHANNGGEE MADEE
                db_com.add_info(self.score.text, self.streaknum.text, self.the_seconds.text)
                db_imp.compare_values_comb(self.score.text, str(self.a_the_streak), self.the_seconds.text)

            else:
                db_com.add_info(self.score.text, '0', self.the_seconds.text)
                db_imp.compare_values_comb(self.score.text, '0', self.the_seconds.text)

        if hello is True:
            if self.total_question > 0:  # if the player decided to leave the game mid way
                self.quit_popup()
                self.no_ques.text = "'Every expert was once \na beginner.'"
                self.no_ques.font_size = 19
                self.no_ques2.text = "-Rutherford Hayes"
                self.no_ques2.font_size = 14
                self.no_ques2.pos_hint = {'center_x': 0.7, 'center_y': 0.4}
            else:
                self.quit_popup()

    def scorechange(self):  # method for the add the score
        score = int(self.score.text)
        if db_imp.new_combine_score(score):
            print("into hometown")
            if score < 10:
                self.score_anim()
                print("we in the small leagues", self.score.text)
                self.ids.final_score.text = ('0' + self.score.text)

            else:
                self.score_anim()
                print("we in the big leagues", self.score.text)
                self.ids.final_score.text = self.score.text

        else:
            self.ids.final_score.opacity = 1
            if score < 10:
                self.ids.final_score.text = ('0' + self.score.text)
            else:
                self.ids.final_score.text = self.score.text

    def question_timer(self, timepassed):
        if self.streak < 2:
            self.progressbar.value = self.progressbar.value - 0.95  # 5 seconds, 95
        elif 2 <= self.streak < 4:
            self.progressbar.value = self.progressbar.value - 0.825  # 6 seconds
        elif 4 <= self.streak < 7:
            self.progressbar.value = self.progressbar.value - 0.773  # 6.5 seconds
        elif 7 <= self.streak < 9:
            self.progressbar.value = self.progressbar.value - 0.7125  # 7 seconds
        elif 9 <= self.streak < 15:
            self.progressbar.value = self.progressbar.value - 0.60725  # 8 seconds
        elif self.streak >= 15:
            self.progressbar.value = self.progressbar.value - 0.5  # 10 seconds

        if self.progressbar.value == 0:
            if self.operator.text == "+":
                reg_sum = int(self.top_num.text) + int(self.bot_num.text)
            elif self.operator.text == "-":
                reg_sum = int(self.top_num.text) - int(self.bot_num.text)

            if self.answer.text != "":
                if int(self.answer.text) == reg_sum:
                    print("your answer:", self.answer.text)
                    print("the real ans: ", reg_sum)
                    print("top_num: ", self.top_num.text)
                    print("bot_num: ", self.bot_num.text)
                    self.right_answers = self.right_answers + 1
                    self.total_question = self.total_question + 1
                    self.progressbar.value = 100
                    self.button_check = False
                    self.right_music(MDApp.get_running_app().volume)
                    self.motivation()
                    self.scorean_card()
                    self.streakcounter()
                    if self.streak < 2:
                        self.scorean(1)
                    elif 2 <= self.streak < 5:
                        self.scorean(2)
                    elif 5 <= self.streak < 9:
                        self.scorean(4)
                    elif 9 <= self.streak < 15:
                        self.scorean(5)
                    self.combine()
                else:
                    self.total_question = self.total_question + 1
                    self.top_nd_bot(self.top_num.text, self.bot_num.text, self.answer.text, reg_sum, self.operator.text)
                    self.streak = 0
                    self.combine()
                    self.clear()
                    self.depression()
                    self.scorered_card()
                    self.progressbar.value = 100
            else:
                #   self.top_nd_bot(self.top_num.text, self.bot_num.text, "-", reg_sum, self.operator.text)
                self.total_question = self.total_question + 1
                self.streak = 0
                self.combine()
                self.clear()
                self.depression()
                self.scorered_card()
                self.progressbar.value = 100

    def on_pre_enter(self, *args):
        self.when_opened()
        db_com.load()

    def on_enter(self):  # on entering the page this what should show up first
        self.answer.opacity = 0
        self.next.opacity = 0
        self.top_num.opacity = 0
        self.bot_num.opacity = 0
        self.operator.opacity = 0
        self.fadein_img()
        self.animations_roll()
        self.combine()
        self.question_timer(3)
        self.timer_1 = Clock.schedule_interval(self.countdown, 1)  # the 3,2,1 GO
        self.timer_2 = Clock.schedule_interval(self.clkwork, 1)  # the countdown from 60seconds
        self.timer_3 = Clock.schedule_interval(self.popupbox, 1)  # time for the popup box
        Clock.schedule_interval(self.question_timer, 0.05)
        db_imp.load()

    def reset(self):
        self.popup.my_x_hint = -0.5
        Clock.unschedule(self.countdown)
        Clock.unschedule(self.clkwork)
        Clock.unschedule(self.popupbox)
        Clock.unschedule(self.question_timer)

    def when_opened(self):
        self.total_question = 0
        self.right_answers = 0
        self.list = []
        self.ttop = []
        self.bbot = []
        self.user_ans = []
        self.real_ans = []
        self.fire_list = []
        self.joined_eq = []
        self.question_part.clear_widgets()
        self.answer_part.clear_widgets()
        self.realanswer_part.clear_widgets()
        self.ctdown = 64  # for the visible countdown timer
        self.ctdown2 = 65  # for the countdown whe the "result score" popup box shows up
        self.streak = 0  # counts the streak
        self.thescore = 0  # the score of the player
        self.score.text = "0"
        self.count = 4  # the 3,2,1, GO! timer
        self.a_the_streak = 0
        self.button_check = False
        self.time.font_size = '250sp'
        self.grid.disabled = False
        self.backspace.disabled = False
        self.answer.disabled = False
        self.next.disabled = False
        self.scolbl.opacity = 1
        self.top_num.text = ""
        self.bot_num.text = ""
        self.xae.disabled = False
        self.clock_name.opacity = 1
        self.clock_name.font_size = '15sp'
        self.clock.font_size = '20sp'
        self.clock_name.color = (39 / 255, 245 / 255, 242 / 255, 1)
        self.clock.color = (1, 1, 1, 1)
        self.back_card.line_color = (248 / 255, 181 / 255, 12 / 255, 0)
        self.back_card2.line_color = (248 / 255, 181 / 255, 12 / 255, 0)
        self.back_card3.line_color = (248 / 255, 181 / 255, 12 / 255, 0)

    def on_leave(self, *args):
        self.reset()
        self.answer.text = ''
        self.no_ques.opacity = 0
        self.no_ques2.opacity = 0
        self.time_label.opacity = 1
        self.the_seconds.opacity = 1
        self.aq.opacity = 1
        self.attempts.opacity = 1
        self.thescore_label.opacity = 1
        self.percentage.opacity = 1
        self.end_streak.opacity = 1
        self.streaknum.opacity = 1
        self.swipeupicon.opacity = 1
        self.swipeup.opacity = 1
        self.back_card.opacity = 1
        self.back_card2.opacity = 1
        self.back_card3.opacity = 1
        self.ids.scroller.scroll_y = 1
        self.samurai.opacity = 1
        self.samurai_two.opacity = 0
        self.the_seconds.color = (1, 1, 1, 1)
        self.ids.final_score.color = (1, 1, 1, 1)
