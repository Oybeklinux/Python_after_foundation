from kivy.app import App
from kivy.core.window import Window
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle, Ellipse
from kivy.metrics import dp
from kivy.properties import Clock
from kivy.uix.button import Button
from kivy.uix.widget import Widget


# Window.size = (600,600)

class MainWidget(Widget):
    distance_x = 3
    distance_y = 3
    button = 1
    add = True
    add_y = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(rgb=(1, 0, 1))
            self.rec = Ellipse(pos=(100,0), size=(dp(100), dp(100)))
            Clock.schedule_interval(self.move, 0.01)

    def button_clicked(self, value):
        self.button =1#*= value
        self.move(1)

    # def on_size(self, *args):
    #     self.rec.pos=(self.center_x - self.rec.size[0]/2, self.center_y - self.rec.size[1]/2)

    def move(self, dt):
        x, y = self.rec.pos

        x += self.distance_x
        y += self.distance_y



        if x + self.rec.size[0] > self.width:
            x = self.width - self.rec.size[0]
            self.distance_x = -self.distance_x
        if y + self.rec.size[1] > self.height:
            y = self.height - self.rec.size[1]
            self.distance_y = -self.distance_y
        if x < 0:
            x = 0
            self.distance_x = -self.distance_x
        if y < 0:
            y = 0
            self.distance_y = -self.distance_y

        self.rec.pos = (x, y)


class MainApp(App):
    pass


MainApp().run()