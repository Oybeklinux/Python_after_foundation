

class Client:

    def __init__(self, id=None, name=None, address=None, birth_date=None):
        self.id = id
        self.name = name
        self.address = address
        self.birth_date = birth_date

    def __str__(self):
        return f"""
Mijoz:        
id: {self.id}
name: {self.name}
address: {self.address}
birth date: {self.birth_date}"""
# card: {self.card}