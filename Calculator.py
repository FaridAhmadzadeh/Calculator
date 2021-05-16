import math
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class Calc(GridLayout):
    def cal(self, event):
        calc_index = self.display.text
        try:
            for num in calc_index:
                if num == '*' or num == '+' or num == '/' or num == '-':
                    if event:
                        try:
                            print(event)
                            self.display.text = str(eval(event))
                            self.dis_en_button(True)
                        except:
                            self.display.text = "ERROR"
                            self.dis_en_button(True)
        except:
            self.display.text = "ERROR"
            self.dis_en_button(True)

    def clear_behv(self):
        self.dis_en_button(False)

    def dis_en_button(self, status):
        for button in self.buttons:
            button.disabled = status

    def number_root(self, event):
        if event:
            try:
                root = math.sqrt(int(event))
                self.display.text = str(root)
                self.dis_en_button(True)
            except:
                self.display.text = 'ERROR'
                self.dis_en_button(True)

    def factoriel(self, event):
        if event:
            try:
                fact = math.factorial(int(event))
                self.display.text = str(fact)
                self.dis_en_button(True)
            except:
                self.display.text = 'ERROR'
                self.dis_en_button(True)

    def tan_x(self, event):
        if event:
            try:
                tan = math.tan(int(event))
                self.display.text = str(tan)
                self.dis_en_button(True)
            except:
                self.display.text = "ERROR"
                self.dis_en_button(True)

    def sin_x(self, event):
        if event:
            try:
                sin = math.sin(int(event))
                self.display.text = str(sin)
                self.dis_en_button(True)
            except:
                self.display.text = "ERROR"
                self.dis_en_button(True)

    def cos_x(self, event):
        if event:
            try:
                cos = math.cos(int(event))
                self.display.text = str(cos)
                self.dis_en_button(True)
            except:
                self.display.text = "ERROR"
                self.dis_en_button(True)

    def log_x(self, event):
        if event:
            try:
                log = math.log10(int(event))
                self.display.text = str(log)
                self.dis_en_button(True)
            except:
                self.display.text = "ERROR"
                self.dis_en_button(True)


class Calculator(App):
    def build(self):
        self.load_kv('Calculator.kv')
        return Calc()


if __name__ == '__main__':
    Calculator().run()
