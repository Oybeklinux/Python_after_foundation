from kivy.uix import label
# from kivy.uix.label import Label
from kivymd.uix.label import Label
from kivymd.uix.textfield import TextInput
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable, CellRow
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from dbmanager import DbManager
# from kivy.uix.textinput import TextInput
from items import Product
from datetime import date


class SkladApp(MDApp):


    def build(self):
        self.product = None
        screen = Screen()
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
        box_top = BoxLayout(size_hint=(1, None), height=dp(40), spacing=dp(50))
        box_bottom = BoxLayout()

        button_delete = MDRectangleFlatButton(text="Delete")
        button_add = MDRectangleFlatButton(text="Add")
        button_edit = MDRectangleFlatButton(text="Update")

        button_add.bind(on_press=self.add_product)
        button_edit.bind(on_press=self.update_product)
        button_delete.bind(on_press=self.delete_product)

        box_top.add_widget(button_add)
        box_top.add_widget(button_edit)
        box_top.add_widget(button_delete)

        box_label = BoxLayout(size_hint=(1, None), height=dp(40), spacing=dp(50))

        lbl_name = Label(text='Name', color=(0,0,0,1))
        lbl_created = Label(text='Deadline', color=(0,0,0,1))
        lbl_price = Label(text='Price', color=(0,0,0,1))

        box_label.add_widget(lbl_name)
        box_label.add_widget(lbl_created)
        box_label.add_widget(lbl_price)

        box_txt = BoxLayout(size_hint=(1, None), height=dp(30), spacing=dp(50))

        self.txt_name = TextInput()
        self.txt_deadline = TextInput()
        self.txt_price = TextInput()
        self.txt_date_added = TextInput()

        box_txt.add_widget(self.txt_name)
        box_txt.add_widget(self.txt_deadline)
        box_txt.add_widget(self.txt_price)

        box_bottom.add_widget(self.table)

        box = BoxLayout(orientation="vertical", padding=(dp(10), dp(10)))
        box.add_widget(box_top)
        box.add_widget(box_label)
        box.add_widget(box_txt)
        box.add_widget(box_bottom)

        screen.add_widget(box)
        self.update_table()
        return screen

    def update_table(self):

        row_data = []
        for product in self.db.product_all():
            row_data.append(
                (
                    product.id, product.name, product.deadline, product.price, product.date_added
                )
            )
        self.table.row_data = row_data

    def update_product(self, btn):
        if self.product and self.product.id:

            self.product.price = float(self.txt_price.text)
            self.product.name = self.txt_name.text
            self.product.deadline = date.fromisoformat(self.txt_deadline.text)

            self.db.product_update(self.product)
            self.update_table()

    def delete_product(self, btn):
        for row in self.table.get_row_checks():
            self.db.product_delete(row[0])
        self.update_table()

    def clear(self):
        self.txt_price.text = ""
        self.txt_deadline.text = ""
        self.txt_name.text = ""

    def add_product(self, btn):
        print("Add clicked")
        try:
            price = float(self.txt_price.text)
            deadline = None
            if self.txt_deadline.text:
                deadline = date.fromisoformat(self.txt_deadline.text)
            name = self.txt_name.text

        except Exception as error:
            print("formatda xatolik bor", error)
            return

        product = Product(name=name, deadline=deadline,
                          price=price)
        self.db.product_insert(product)
        self.update_table()
        self.clear()

    def check_pressed(self, instance_table, current_row):
        print("check_pressed", instance_table, current_row)

    def row_pressed(self, table:MDDataTable, row: CellRow):
        start_index, _ = row.table.recycle_data[row.index]["range"]
        id_ = row.table.recycle_data[start_index]["text"]
        self.product = self.db.product_get(id_)

        self.txt_price.text = str(self.product.price)
        self.txt_name.text = self.product.name
        self.txt_deadline.text = str(self.product.deadline)
        self.txt_date_added.text = str(self.product.date_added)


SkladApp().run()