from kivy.app import App
# from kivy.core.text import Label
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

Window.size = (800, 600)

class GridLayoutWindow(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("sdf")
        self.cols = 4
        self.add_widget(Label(text="Ism sharif", size_hint=(1, None), height=dp(50)))
        self.add_widget(Label(text="Davomat", size_hint=(1, None), height=dp(50)))
        self.add_widget(Label(text="Vazifa", size_hint=(1, None), height=dp(50)))
        self.add_widget(Label(text="SMS", size_hint=(1, None), height=dp(50)))

    # def _read_xlsx(self):


class SmsApp(App):
    pass

SmsApp().run()