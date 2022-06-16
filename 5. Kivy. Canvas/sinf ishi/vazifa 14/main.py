from kivy.app import App
from time import sleep
from kivy.core.window import Window
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.metrics import dp
from kivy.properties import Clock
from kivy.uix.widget import Widget

Window.size = (800, 600)



class CanvasExample10(Widget):
    distance = 50
    horizontal = False
    to_right = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(1,0,0)
            self.rect = Ellipse(pos=(0, 0), size=(50, 50))
        Clock.schedule_interval(self.move, 0.1)

    def move_horizontal(self):
        self.horizontal = True

    def move_vertikal(self):
        self.horizontal = False

    def move(self, dt):
        x, y = self.rect.pos
        if self.horizontal:
            if self.to_right:
                if x + self.distance + self.rect.size[0] <= self.width:
                    x += self.distance
                else:
                    self.to_right = False
            else:
                if x - self.distance >= 0:
                    x -= self.distance
                else:
                    self.to_right = True

        self.rect.pos = (x, y)

class mainApp(App):
    pass

mainApp().run()