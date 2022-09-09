
from datetime import date


class Product:

    def __init__(self, id=None, name=None, deadline=None, price=None, date_added=None):
        self.id = id
        if not isinstance(name, str):
            raise Exception('Type error: name shoulb be str')
        self.name: str = name
        if not isinstance(deadline, date):
            deadline = None
        self.deadline: date = deadline
        if not isinstance(price, float) and not isinstance(price, int):
            raise Exception("Type error: price should be number")
        self.price: float = price
        if not isinstance(date_added, date):
            date_added = date.today()
        self.date_added: date = date_added

    def __str__(self):
        return f"""
Mahsulot:        
id: {self.id}        
name: {self.name}
deadline: {self.deadline}
price: {self.price}
date_added: {self.date_added}"""




