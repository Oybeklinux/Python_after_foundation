import os
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.datatables import MDDataTable, CellRow
from dbmanager import DbManager

Window.size = (600, 600)


class SkladApp(MDApp):

    def build(self):
        self.title = "Ombor"
        self.theme_cls.theme_style = "Light"
        return Builder.load_file(
            os.path.join(os.path.dirname(__file__), "./sklad.kv")
        )



class MainWindow(Screen):

    def view_product(self):
        self.db = DbManager()
        column_data = [
            ('id', dp(20)),
            ('name', dp(30)),
            ('deadline', dp(30)),
            ('price', dp(30)),
            ('date added', dp(30))
        ]
        self.table = MDDataTable(
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            size_hint=(1, 1),
            check=True,
            column_data=column_data)
        self.table.bind(on_check_press=self.check_pressed)
        self.table.bind(on_row_press=self.row_pressed)
        box_bottom = MDBoxLayout(size_hint=(1,0.8))
        box_bottom.add_widget(self.table)
        self.add_widget(box_bottom)


    def check_pressed(self, instance_table, current_row):
        print("check_pressed", instance_table, current_row)

    def row_pressed(self, table:MDDataTable, row: CellRow):
        print(row)



class WindowManager(ScreenManager):
    pass


if __name__ == "__main__":
    app = SkladApp()
    app.run()