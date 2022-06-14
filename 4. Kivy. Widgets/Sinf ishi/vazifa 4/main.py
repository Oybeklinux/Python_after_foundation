from kivy.app import App
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
Window.size = (800, 600)


class MainWidget(GridLayout):

    def change_value(self, ctrl):
        print(ctrl.value)


class SoddaApp(App):
    pass

app = SoddaApp()
app.run()