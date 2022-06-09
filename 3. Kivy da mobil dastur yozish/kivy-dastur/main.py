from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout

class WidgetsWindow(GridLayout):
    my_text = StringProperty("Matn")
    counter = 0

    def on_pressed(self):
        self.counter += 1
        print("pressed")
        self.my_text = str(self.counter)

    def on_state_toggle(self, toggle):
        if toggle.state == "down":
            toggle.text = "ON"
        else:
            toggle.text = "OFF"


class StackLayoutWindow(StackLayout):
    def __init__(self, **kwargs):
        self.orientation = "rl-bt"
        self.padding = (dp(20), dp(20), dp(20), dp(20))
        self.spacing = (dp(10), dp(20))
        super().__init__(**kwargs)
        for i in range(1, 100):
            b = Button(text=str(i), size_hint=(None, None), size=(dp(100), dp(100)))
            self.add_widget(b)


class AnchorWindow(AnchorLayout):
    pass

class BoxLayoutWidget(BoxLayout):
    pass

class MainWidget(Widget):
    pass


class MainApp(App):
    pass

MainApp().run()

