from kivy.lang import Builder
from kivy.properties import *
from kivy.lang import Builder
import math
import os


class DatabaseAddition:
    def __init__(self, filename):
        self.filename = filename
        self.scores = None
        self.streaks = None
        self.fastest_time = None
        self.file = None
        self.load()

    def load(self):
        self.file = open(self.filename, "r+")
        self.scores = []
        self.streaks = []
        self.fastest_time = []

        for line in self.file:
            score, streak, fastest = line.strip().split(";")
            self.scores.append(int(score))
            self.streaks.append(int(streak))
            self.fastest_time.append(float(fastest))

    def get_info(self):
        return self.scores, self.streaks, self.fastest_time

    def add_info(self, score, streak, time):
        tup1 = (score, streak, time)
        # Use str.join() to convert tuple to string.
        strings = '; '.join(tup1)
        self.file.write("\n")
        self.file.write(strings)
        self.scores.append(int(score))
        self.streaks.append(int(streak))
        self.fastest_time.append(float(time))

        self.file.close()


class DatabaseSubtraction:
    subtraction_score_input = ObjectProperty(None)
    subtraction_time_input = ObjectProperty(None)
    subtraction_streak_input = ObjectProperty(None)

    def __init__(self, filename):
        self.filename = filename
        self.scores = None
        self.streaks = None
        self.fastest_time = None
        self.file = None
        self.load()

    def load(self):
        self.file = open(self.filename, 'r+')
        self.scores = []
        self.streaks = []
        self.fastest_time = []

        for line in self.file:
            score, streak, time = line.strip().split(';')
            self.scores.append(int(score))
            self.streaks.append(int(streak))
            self.fastest_time.append(float(time))

    def add_info(self, score, streak, time):
        tup1 = (score, streak, time)
        # Use str.join() to convert tuple to string.
        strings = '; '.join(tup1)
        self.file.write("\n")
        self.file.write(strings)
        self.scores.append(int(score))
        self.streaks.append(int(streak))
        self.fastest_time.append(float(time))

        self.file.close()

    def get_info(self):
        return self.scores, self.streaks, self.fastest_time


class DatabaseCombined:
    def __init__(self, filename):
        self.filename = filename
        self.scores = None
        self.streaks = None
        self.fastest_time = None
        self.file = None
        self.load()

    def load(self):
        self.file = open(self.filename, 'r+')
        self.scores = []
        self.streaks = []
        self.fastest_time = []

        for line in self.file:
            score, streak, time = line.strip().split(';')
            self.scores.append(int(score))
            self.streaks.append(int(streak))
            self.fastest_time.append(float(time))

    def add_info(self, score, streak, time):
        tup1 = (score, streak, time)
        # Use str.join() to convert tuple to string.
        strings = '; '.join(tup1)
        self.file.write("\n")
        self.file.write(strings)
        self.scores.append(int(score))
        self.streaks.append(int(streak))
        self.fastest_time.append(float(time))

        self.file.close()

    def get_info(self):
        return self.scores, self.streaks, self.fastest_time


class DatabasePercentage:
    def __init__(self, filename):
        self.filename = filename
        self.scores = None
        self.streaks = None
        self.fastest_time = None
        self.file = None
        self.load()

    def load(self):
        self.file = open(self.filename, "r+")
        self.scores = []
        self.streaks = []
        self.fastest_time = []

        for line in self.file:
            score, streak, fastest = line.strip().split(";")
            self.scores.append(int(score))
            self.streaks.append(int(streak))
            self.fastest_time.append(float(fastest))

    def get_info(self):
        return self.scores, self.streaks, self.fastest_time

    def add_info(self, score, streak, time):
        tup1 = (score, streak, time)
        # Use str.join() to convert tuple to string.
        strings = '; '.join(tup1)
        self.file.write("\n")
        self.file.write(strings)
        self.scores.append(int(score))
        self.streaks.append(int(streak))
        self.fastest_time.append(float(time))
        self.file.close()


class Improvement:      # just the percentage scores 1,2,4
    percent = 0
    count = 0
    fcore = 0
    add_point_score = 0
    add_point_time = 0
    add_point_streak = 0

    sub_point_score = 0
    sub_point_time = 0
    sub_point_streak = 0

    combo_point_score = 0
    combo_point_time = 0
    combo_point_streak = 0
    final_combo_value = 0

    percent_point_score = 0
    percent_point_time = 0
    percent_point_streak = 0

    final_value = 0
    values = []
    parentlist = {}
    sets = 0
    num = 0
    end_result = 0
    summation = 0
    chunked_list = []
    loading_Sets = []
    status = 'disable'

    update_button = ObjectProperty(None)

    def __init__(self, filename):
        self.filename = filename
        self.file = None
        self.load()

    def load(self):
        self.file = open(self.filename, 'r+')
        for line in self.file:
            self.fcore = line.strip().split(';')
            print("fcore: ", self.fcore)
            self.val()
            self.breakdown()
            self.file.seek(0, 2)

    def val(self):
        if os.path.getsize("assets/text/improv.txt") > 0:
            if len(self.fcore) >= 10:
                return True
            else:
                return False
        else:
            self.file.write("0")

    def new_subtract_ans(self, time):
        db_sub = DatabaseSubtraction("assets/text/sub_data.txt")
        time_list = [float(items) for items in db_sub.fastest_time]
        if min(time_list) > time:
            return True
        else:
            return False

    def new_subtract_streak(self, streak):
        db_sub = DatabaseSubtraction("assets/text/sub_data.txt")
        streak_list = [int(items) for items in db_sub.streaks]
        if max(streak_list) < int(streak):
            return True
        else:
            return False

    def new_subtract_score(self, score):
        db_sub = DatabaseSubtraction("assets/text/sub_data.txt")
        score_list = [int(items) for items in db_sub.scores]
        if max(score_list) < int(score):
            return True
        else:
            return False

    def new_percent_ans(self, time):
        db_per = DatabasePercentage("assets/text/percent_data.txt")
        time_list = [float(items) for items in db_per.fastest_time]
        if min(time_list) > time:
            return True
        else:
            return False

    def new_percent_streak(self, streak):
        db_per = DatabasePercentage("assets/text/percent_data.txt")
        streak_list = [int(items) for items in db_per.streaks]
        if max(streak_list) < int(streak):
            return True
        else:
            return False

    def new_percent_score(self, score):
        db_per = DatabasePercentage("assets/text/percent_data.txt")
        score_list = [int(items) for items in db_per.scores]
        if max(score_list) < int(score):
            return True
        else:
            return False

    def new_combine_ans(self, time):
        db_com = DatabaseCombined("assets/text/com_data.txt")
        time_list = [float(items) for items in db_com.fastest_time]
        if min(time_list) > time:
            return True
        else:
            return False

    def new_combine_streak(self, streak):
        db_com = DatabaseCombined("assets/text/com_data.txt")
        streak_list = [int(items) for items in db_com.streaks]
        if max(streak_list) < int(streak):
            return True
        else:
            return False

    def new_combine_score(self, score):
        db_add = DatabaseAddition("assets/text/add_data.txt")
        score_list = [int(items) for items in db_add.scores]
        print("got into dabase")
        if max(score_list) < int(score):
            print("All approved. ship back")
            return True
        else:
            print("failure")
            return False

    def new_addition_score(self, score):
        db_add = DatabaseAddition("assets/text/add_data.txt")
        score_list = [int(items) for items in db_add.scores]
        if max(score_list) < int(score):
            return True
        else:
            return False

    def new_addition_ans(self, time):
        db_add = DatabaseAddition("assets/text/add_data.txt")
        time_list = [float(items) for items in db_add.fastest_time]
        if min(time_list) > time:
            return True
        else:
            return False

    def new_addition_streak(self, streak):
        db_add = DatabaseAddition("assets/text/add_data.txt")
        streak_list = [int(items) for items in db_add.streaks]
        if max(streak_list) < int(streak):
            return True
        else:
            return False

    def compare_values_addition(self, score, streak, time):
        db_add = DatabaseAddition("assets/text/add_data.txt")

        time_list = [float(items) for items in db_add.fastest_time]
        streak_list = [int(items) for items in db_add.streaks]
        score_list = [int(items) for items in db_add.scores]

        del score_list[-1]
        del time_list[-1]
        del streak_list[-1]

        new_score = int(score)
        new_streak = int(streak)
        new_time = float(time)

        if max(score_list) < new_score:
            self.add_point_score = 2
            print("ADD SCOORREEEE")
        if min(time_list) > new_time:
            self.add_point_time = 2
            print("ADD TIMEEE")
        if max(streak_list) < new_streak:
            self.add_point_streak = 2
            print("ADD STREAKKKK")

        self.tallyScore(self.add_point_score, self.add_point_time, self.add_point_streak)

    def compare_value_sub(self, score, streak, time):
        db_sub = DatabaseSubtraction('assets/text/sub_data.txt')

        sub_time_list = [float(items) for items in db_sub.fastest_time]
        sub_streak_list = [int(items) for items in db_sub.streaks]
        sub_score_list = [int(items) for items in db_sub.scores]

        del sub_score_list[-1]
        del sub_time_list[-1]
        del sub_streak_list[-1]

        sub_new_score = int(score)
        sub_new_streak = int(streak)
        sub_new_time = float(time)

        if max(sub_score_list) < sub_new_score:
            self.sub_point_score = 2
            print("SUB SCOORREEEE")
        if min(sub_time_list) > sub_new_time:
            self.sub_point_time = 2
            print("SUB TIMEEE")
        if max(sub_streak_list) < sub_new_streak:
            self.sub_point_streak = 2
            print("SUB STREAKKKK")
        self.tallyScore(self.sub_point_score, self.sub_point_time, self.sub_point_streak)

    def compare_values_comb(self, score, streak, time):
        db_com = DatabaseCombined("assets/text/com_data.txt")

        time_list = [float(items) for items in db_com.fastest_time]
        streak_list = [int(items) for items in db_com.streaks]
        score_list = [int(items) for items in db_com.scores]

        del score_list[-1]
        del time_list[-1]
        del streak_list[-1]

        comb_new_score = int(score)
        comb_new_streak = int(streak)
        comb_new_time = float(time)

        if max(score_list) < comb_new_score:
            self.combo_point_score = 2
            print("COM SCOORREEEE")
        if min(time_list) > comb_new_time:
            self.combo_point_time = 2
            print("COM TIMEEE")
        if max(streak_list) < comb_new_streak:
            self.combo_point_streak = 2
            print("COM STREAKKKK")

        self.tallyScore(self.combo_point_score, self.combo_point_time, self.combo_point_streak)

    def compare_values_percentage(self, score, streak, time):
        db_per = DatabasePercentage("assets/text/percent_data.txt")

        time_list = [float(items) for items in db_per.fastest_time]
        streak_list = [int(items) for items in db_per.streaks]
        score_list = [int(items) for items in db_per.scores]

        del score_list[-1]
        del time_list[-1]
        del streak_list[-1]

        new_score = int(score)
        new_streak = int(streak)
        new_time = float(time)

        if max(score_list) < new_score:
            self.percent_point_score = 2
            print("PER SCOORREEEE")
        if min(time_list) > new_time:
            self.percent_point_time = 2
            print("PER TIMEEE")
        if max(streak_list) < new_streak:
            self.percent_point_streak = 2
            print("PER STREAKKKK")

        self.tallyScore(self.percent_point_score, self.percent_point_time, self.percent_point_streak)

    def tallyScore(self, score, time, streak):
        highScore = int(score)
        highTime = int(time)
        highStreak = int(streak)

        self.total = highScore + highStreak + highTime
        if self.total >= 4:
            self.final_value = 4
            tuple = (";", str(self.final_value))
            joined_tuple = ''.join(tuple)
            self.file.seek(0, 2)
            self.file.write(joined_tuple)

        elif 1 < self.total < 4:
            self.final_value = self.total
            tuple = (";", str(self.final_value))
            joined_tuple = ''.join(tuple)
            self.file.seek(0, 2)
            self.file.write(joined_tuple)

        else:
            self.final_value = 1
            tuple = (";", str(self.final_value))
            joined_tuple = ''.join(tuple)
            self.file.seek(0, 2)
            self.file.write(joined_tuple)

        self.file.close()

    def breakdown(self):
        self.sets = (math.ceil(len(self.fcore) / 10) + 1)
        #print("length of the fcore list:", len(self.fcore))
        #print("self.sets: ", self.sets)
        self.chunked_list = list()
        chunk_size = 10
        for i in range(0, len(self.fcore), chunk_size):
            self.chunked_list.append(self.fcore[i:i+chunk_size])
        #print("chunked_list: ", self.chunked_list)

    # def disabler(self):
    #     if self.sets == 3:
    #         return True
    #     else:
    #         return False

    def updatedCal(self):
        self.loading_Sets.clear()
        self.load()
        #self.disabler()
        if os.path.getsize("assets/text/improv.txt") > 0:
            if len(self.chunked_list[0]) >= 10:
                for i in range(0, self.sets - 1):
                    self.num = 0
                    for value, j in enumerate(self.chunked_list[i]):
                        if j == str(4):
                            self.num += 1
                            if self.num >= 2:
                                element_value = str(6)
                                self.loading_Sets.append(element_value)
                                self.num = 0
                                break
                    else:
                        ints = [int(item) for item in self.chunked_list[i]]
                        highvalue = max(ints)
                        self.loading_Sets.append(highvalue)

            else:
                return False, False
        else:
            self.file.write("0")
            return False, False
    #print("chunked_Set: ", self.chunked_list)
        #print("the top sets:", self.loading_Sets)
    #print("chunked list length:", len(self.chunked_list[0]))

        if len(self.chunked_list[0]) >= 10:
            del self.fcore[:10]
            del self.chunked_list[0]
#            print("length of fcore rn: ", len(self.fcore))

            print("pass!")
            db_new = NewClass('assets/text/end_score.txt')
            db_new.load(self.fcore)
            self.summation = self.loading_Sets[0]
            #print("deleted fcore: ", self.fcore)
            #print("deleted chunk_Set: ", self.chunked_list)

            cp = theEnd('assets/text/end_score.txt')
            current_value = cp.load()
            #print("current value percent: ", current_value)
            #print("current summation: ", self.summation)
            return int(current_value), int(self.summation)
        else:
            print("play atleast 10 games")
            cp = theEnd('assets/text/end_score.txt')
            current_value = cp.load()
            return int(current_value), "0"


class theEnd:
    the_end_score = 0
    the_percentage = 0

    def __init__(self, filename):
        self.filename = filename
        self.file = None
        self.load()

    def load(self):
        self.file = open(self.filename, 'r+')
        for line in self.file:
            self.the_end_score = line.strip().split(";")
            return self.the_end_score[-1]

    def rewrite(self, value):
        tuple = (";", str(value))
        join_tuple = ''.join(tuple)
        self.file.write(join_tuple)
        self.file.close()


class NewClass:
    new_fcore = []

    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def load(self, list):
        new_fcore = list
        print("New_Class fcore:", new_fcore)
        self.file = open("assets/text/improv.txt", 'w')
        for value, element in enumerate(new_fcore):
            if value == len(new_fcore) - 1:
                self.file.write(element)
            else:
                self.file.write(element + ";")
        self.file.close()
