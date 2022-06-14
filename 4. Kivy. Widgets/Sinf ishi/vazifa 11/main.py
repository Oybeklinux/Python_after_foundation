from kivy.app import App
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
Window.size = (800, 600)


class MainWidget(GridLayout):
    name = StringProperty("")

    def name_entered(self, textinput):
        self.name = textinput.text


class SoddaApp(App):
    pass


app = SoddaApp()
app.run()