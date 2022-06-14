from kivy.app import App
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
Window.size = (800, 600)


class MainWidget(GridLayout):
    counter = StringProperty("")
    count_enabled = BooleanProperty(False)
    incremention = 0

    def change_state(self, ctrl):
        if ctrl.state == 'down':
            ctrl.text = "ON"
            self.count_enabled = True
        else:
            self.count_enabled = False
            ctrl.text = "OFF"

    def increase(self):
        if self.count_enabled:
            self.incremention += 1
            self.counter = str(self.incremention)


class SoddaApp(App):
    pass

app = SoddaApp()
app.run()