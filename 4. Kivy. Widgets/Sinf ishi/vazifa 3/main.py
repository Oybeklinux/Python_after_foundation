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
        self.count_enabled = ctrl.active

    def increase(self):
        if self.count_enabled:
            self.incremention += 1
            self.counter = str(self.incremention)


class SoddaApp(App):
    pass

app = SoddaApp()
app.run()