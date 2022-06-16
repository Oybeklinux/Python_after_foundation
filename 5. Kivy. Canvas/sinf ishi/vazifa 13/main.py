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
    distance = 10
    choise = 1

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(1,0,0)
            self.rect = Rectangle(pos=(300,230), size=(50, 50))

        Clock.schedule_interval(self.yangila, 1)

    def move_right(self):
        self.choise = 1

    def move_left(self):
        pass

    def move_top(self):
        pass

    def move_bottom(self):
        pass

    def yangila(self, dt):
        x, y = self.rect.pos
        if self.choise == 1:
            if x + self.distance + self.rect.size[0] <= self.width:
                x += self.distance
                self.rect.pos = (x, y)


class mainApp(App):
    pass

mainApp().run()