from kivy.app import App
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
Window.size = (800, 600)


class MainWidget(GridLayout):
    pass
    # counter = StringProperty("")
    #
    # def change_value(self, ctrl):
    #     self.counter = str(int(ctrl.value))


class SoddaApp(App):
    pass


app = SoddaApp()
app.run()