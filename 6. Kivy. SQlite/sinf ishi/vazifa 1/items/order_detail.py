class OrderDetail:

    def __init__(self, product, total, order_id=None, id=None):
        self.id = id
        self.product = product
        self.total = total
        self.order_id = order_id

    def __str__(self):
        return f"""
Detallar:        
id: {self.id}
product: {self.product}
total: {self.total}
order_id: {self.order_id}"""

