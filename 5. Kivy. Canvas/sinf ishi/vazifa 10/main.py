from kivy.app import App

from kivy.core.window import Window
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.metrics import dp
from kivy.uix.widget import Widget

Window.size = (800, 600)

class CanvasExample(Widget):
    pass

class CanvasExample10(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(0,0,100,100,100,200,300,200))
            Color(1,0,0)
            Rectangle(pos=(100,230), size=(100, 200))
            Color(0,1,0)
            Ellipse(pos=(300,200), size=(50,100))
            Line(rectangle=(300,100, 50,50), width=dp(2))

class mainApp(App):
    pass

mainApp().run()