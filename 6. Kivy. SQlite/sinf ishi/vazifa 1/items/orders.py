from .product import Product
from .client import Client
from .order_detail import OrderDetail


class Orders:

    def __init__(self, id=None, client: Client=None, added_date=None, order_details:list[OrderDetail]=None, status=False):
        self.id = id
        self.client = client
        self.added_date = added_date
        self.status = status
        self.order_details = order_details

    def __str__(self):
        text = f"""
Buyurtma:        
id: {self.id}
date_added: {self.added_date}
status: {self.status}
"""
        for order_detail in self.order_details:
            text += f"""{order_detail}\n"""
        return text