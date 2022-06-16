from kivy.app import App

from kivy.core.window import Window
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.metrics import dp
from kivy.uix.widget import Widget

Window.size = (800, 600)


class CanvasExample10(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(1,0,0)
            self.rect = Rectangle(pos=(300,230), size=(50, 50))

    def move(self):
        # Koordinatasini o'zgartirish
        self.rect.pos = (400, 400)

    def move_right(self):
        x, y = self.rect.pos
        if x + 100 + self.rect.size[0] <= self.width:
            x += 100

        self.rect.pos = (x, y)

class mainApp(App):
    pass

mainApp().run()