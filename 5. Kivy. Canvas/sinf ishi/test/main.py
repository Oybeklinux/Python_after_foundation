from kivy.app import App

from kivy.core.window import Window
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle, Ellipse
from kivy.properties import Clock
from kivy.uix.widget import Widget

Window.size = (800, 600)


class Task1(Widget):
    pass

class Task7(Widget):
    distance = 50
    horizontal = False
    to_right = True
    to_top = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(1,0,0)
            self.rect = Ellipse(pos=(0, 0), size=(50, 50))
        Clock.schedule_interval(self.move, 0.1)

    def move_horizontal(self):
        self.horizontal = True

    def move_vertical(self):
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
        else:
            if self.to_top:
                if y + self.distance + self.rect.size[1] <= self.height:
                    y += self.distance
                else:
                    self.to_top = False
            else:
                if y - self.distance >= 0:
                    y -= self.distance
                else:
                    self.to_top = True

        self.rect.pos = (x, y)


class Task6(Widget):
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


class Task5(Widget):
    distance = 10

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(1,0,0)
            self.rect = Rectangle(pos=(300, 230), size=(50, 50))

    def move_center(self):
        x, y = self.rect.pos
        x = self.width/2 - self.rect.size[1] / 2
        y = self.height/2 - self.rect.size[1] / 2
        self.rect.pos = (x, y)

    def move_left(self):
        x, y = self.rect.pos
        if x - self.distance >= 0:
            x -= self.distance

        self.rect.pos = (x, y)

    def move_top(self):
        x, y = self.rect.pos
        if y + self.distance + self.rect.size[1] <= self.height:
            y += self.distance

        self.rect.pos = (x, y)

    def move_bottom(self):
        x, y = self.rect.pos
        if y - self.distance >= 0:
            y -= self.distance

        self.rect.pos = (x, y)

    def move_right(self):
        x, y = self.rect.pos
        if x + self.distance + self.rect.size[0] <= self.width:
            x += self.distance

        self.rect.pos = (x, y)

class mainApp(App):
    pass

mainApp().run()