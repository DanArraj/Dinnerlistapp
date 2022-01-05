import random
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
#Window.size = (280,580)

class MainWindow(Screen):
    pass

class GetWindow(Screen):
    def on_enter(self, *args):
        dinners_str = read_dinners()
        self.ids.getdin_label.text = dinners_str
        self.ids.getdin_textInput.text = '0'

    def num_up(self):
        num = int(self.ids.getdin_textInput.text)
        num += 1
        self.ids.getdin_textInput.text = str(num)

    def num_down(self):
        num = int(self.ids.getdin_textInput.text)
        if num > 0:
            num -= 1
        self.ids.getdin_textInput.text = str(num)


    def get_dinners(self):
        dinner_choices = []
        dinner_choices_str = ''
        din_num = int(self.ids.getdin_textInput.text)
        dinners_list = read_dinners().split('\n')
        dinners_list.remove('')
        if din_num > len(dinners_list):
            din_num = len(dinners_list)
        while din_num > 0:
            choice = random.choice(dinners_list)
            if choice in dinner_choices:  # if already slected grab a new chioce
                continue
            dinner_choices.append(choice)
            din_num -= 1
        for dinner in dinner_choices:
            dinner_choices_str += dinner
            dinner_choices_str += '\n'
            self.ids.getdin_label.text = dinner_choices_str

class ModifyWindow(Screen):
    def on_enter(self, *args):
        dinners_str = read_dinners()
        self.ids.moddin_label.text = dinners_str

    def add(self):
        dinners_add_list = (self.ids.moddin_textInput.text).split('\n')
        add_dinners(dinners_add_list)
        dinners_str = read_dinners()
        self.ids.moddin_textInput.text = ''
        self.ids.moddin_label.text = dinners_str

    def remove(self):
        dinners_remove_list = (self.ids.moddin_textInput.text).split('\n')
        dinners_list = read_dinners().split('\n')
        #go through both lists and remove items from dinners_list that are on both - check if there is an easier way
        for dinner_remove in dinners_remove_list:
            for dinner_current in dinners_list:
                if dinner_remove == dinner_current:
                    dinners_list.remove(dinner_remove)
        #overwrite dinner file with list excluding items to be removed
        din_file = open('Dinners.txt', 'w')
        for dinner in dinners_list:
            if dinner != '':
                din_file.write(dinner.strip())
                din_file.write('\n')
        din_file.close()

        dinners_str = read_dinners()
        self.ids.moddin_textInput.text = ''
        self.ids.moddin_label.text = dinners_str

def read_dinners():
    din_file = open('Dinners.txt', 'r')
    dinners_str = din_file.read()
    din_file.close()
    return dinners_str

def add_dinners(dinners_add_list):
    din_file = open('Dinners.txt', 'a')
    for dinner in dinners_add_list:
        if dinner != '':
            din_file.write(dinner.strip())
            din_file.write('\n')
    din_file.close()

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('dinner.kv')

class dinnerApp(App):
    def build(self):
        return kv

if __name__ == '__main__':
    dinnerApp().run()