import sqlite3
from datetime import date, datetime
from items import Product, Client, Orders, OrderDetail


class DbManager:

    def __init__(self):
        self.__open_db()

    def __create_tables(self):
        try:
            self.conn.execute('''
            insert into product(name,price)
            values('test', 1000)
            ''')
            self.conn.rollback()
        except sqlite3.OperationalError as error:
            print('Create table', error)
            self.conn.execute('''
            CREATE TABLE product (
                id integer PRIMARY KEY AUTOINCREMENT,
                name varchar,
                deadline date,
                price real,
                date_added date
                );''')
            self.conn.execute('''
            CREATE TABLE client (
                id integer PRIMARY KEY AUTOINCREMENT,
                name varchar,
                address varchar,
                birth_date date
            );''')
            self.conn.execute('''
            CREATE TABLE orders (
                id integer PRIMARY KEY AUTOINCREMENT,
                created datetime,
                client_id integer,
                status bool, -- True sotildi, False - zakaz qilingi                
                CONSTRAINT fk_client1 FOREIGN KEY (client_id) REFERENCES client (id)                
            );''')
            self.conn.execute('''
            CREATE TABLE order_detail(
                id integer PRIMARY KEY AUTOINCREMENT,
                orders_id integer,
                product_id integer,
                total integer,
                CONSTRAINT fk_product FOREIGN KEY (product_id) REFERENCES product (id)
            );''')
            self.conn.commit()

    def __open_db(self):
        self.conn = sqlite3.connect('test.sqlite')
        self.cursor = self.conn.cursor()
        print("Database opened")
        self.__create_tables()

    def __print_db_path(self):
        for id_, name, filename in self.conn.execute('PRAGMA database_list'):
            if name == 'main' and filename is not None:
                print(filename)
                break

    def __close_db(self):
        self.conn.close()
        print("Database closed")

    def __del__(self):
        self.__close_db()

    def product_insert(self, product: Product):
        """
        Insert new product
        :param product:
        :return: inserted Product
        """
        if not product.date_added:
            product.date_added = date.today()

        SQL = 'INSERT INTO product(name, deadline,price,date_added) ' \
              'VALUES(?,?,?,?)'
        params = (product.name, product.deadline, product.price, product.date_added)

        try:
            row = self.cursor.execute(SQL, params)
            self.conn.commit()
            product.id = row.lastrowid
            return product
        except Exception as error:
            return None

    def product_update(self, product: Product):
        """
        Update product
        :param product:
        :return: updated Product
        """
        if not product.id:
            raise Exception('product id should not be None')
        SQL = """UPDATE product SET name=?, deadline=?,price=?,date_added=?
                WHERE id=?
        """
        params = (product.name, product.deadline, product.price, product.date_added,
                  product.id)
        try:

            self.cursor.execute(SQL, params)
            self.conn.commit()
            print(f"Product {product.name} updated")
            return product
        except Exception as error:
            print(error)
            return None

    def product_delete(self, id):
        '''
        Delete product
        :param: id - product id
        :return: None
        '''
        SQL = """DELETE FROM product 
                WHERE id=?"""
        params = (id,)
        try:
            row = self.cursor.execute(SQL, params)
            if row.lastrowid == id:
                print(f'Product id={row.lastrowid} deleted')
            else:
                print("There is no such id in product table")
            self.conn.commit()
        except Exception as error:
            print(error)

    def product_get(self, id):
        """
        Get product
        :param id: product id
        :return: Product
        """
        SQL = "SELECT * FROM product WHERE id=?"
        params = (id,)
        try:
            self.cursor.execute(SQL, params)
            row = self.cursor.fetchone()
            if row:
                deadline = date.fromisoformat(row[2]) if row[2] else ""
                date_added = date.fromisoformat(row[4]) if row[4] else ""
                product = Product(id=row[0],name=row[1], deadline=deadline,
                                  price=row[3], date_added=date_added)
                return product
            else:
                return None
        except Exception as error:
            print(error)
            return None

    def product_all(self):
        """
        get all product
        :return: list[Product]
        """
        SQL = "SELECT * FROM product"
        products = []
        self.cursor.execute(SQL)
        rows = self.cursor.fetchall()

        for row in rows:
            deadline = date.fromisoformat(row[2]) if row[2] else None
            date_added = date.fromisoformat(row[4]) if row[4] else None
            product = Product(id=row[0], name=row[1], deadline=deadline,
                              price=row[3], date_added=date_added)
            products.append(product)
        return products

    def client_insert(self, client: Client):
        """
        insert client
        :return: inserted Client
        """
        SQL = 'INSERT INTO client(name, address, birth_date) ' \
              'VALUES(?,?,?)'
        params = (client.name, client.address, client.birth_date)

        try:
            row = self.cursor.execute(SQL, params)
            self.conn.commit()
            client.id = row.lastrowid
            print(f"Client {client.name} saved")
            return client
        except Exception as error:
            print(error)
            return None

    def client_update(self, client: Client):
        """
        update client
        :param client: Client
        :return: updated Client
        """
        tmp = self.client_get(client.id)
        if not tmp:
            print("Xatolik client id bo'lishi kerak")
            return None

        client.name = client.name if client.name else tmp.name
        client.address = client.address if client.address else tmp.address
        client.birth_date = client.birth_date if client.birth_date else tmp.birth_date

        SQL = """UPDATE client SET name=?, address=?, birth_date=?
                WHERE id=?
        """
        params = (client.name, client.address, client.birth_date,
                  client.id)
        try:

            self.cursor.execute(SQL, params)
            self.conn.commit()
            print(f"Client {client.name} updated")
            return client
        except Exception as error:
            print(error)
            return None

    def client_delete(self, id):
        """
        delete client
        :param id: client id
        :return:
        """
        SQL = """DELETE FROM client WHERE id=?"""
        params = (id,)
        try:
            row = self.cursor.execute(SQL, params)
            # rowcount - total of deleted rows
            if row.rowcount > 0:
                print(f'Client id={id} deleted: {row.rowcount} ta')
            else:
                print("Bunday mijoz mavjud emas")
            self.conn.commit()
        except Exception as error:
            print(error)

    def client_get(self, id):
        """
        Get Client
        :param id: client id
        :return: Client
        """
        SQL = "SELECT id, name, address,birth_date FROM client WHERE id=?"
        params = (id,)
        try:
            self.cursor.execute(SQL, params)
            row = self.cursor.fetchone()
            if row:
                client = Client(id=row[0], name=row[1], address=row[2], birth_date=date.fromisoformat(row[3]))
                return client
            else:
                return None
        except Exception as error:
            print(error)
            return None

    def client_all(self):
        """
        get all client
        :return: list[Client]
        """
        SQL = "SELECT * FROM client"
        items = []
        self.cursor.execute(SQL)
        rows = self.cursor.fetchall()

        for row in rows:
            item = Client(id=row[0], name=row[1], address=row[2], birth_date=date.fromisoformat(row[3]))
            items.append(item)
        return items

    def order_detail_insert(self, order_detail: OrderDetail):
        """
        Insert order detail
        :param order_detail: OrderDetail
        :param order_id: order id
        :return: inserted OrderDetail
        """

        SQL = 'INSERT INTO order_detail(orders_id, product_id, total) ' \
              'VALUES(?,?,?)'
        try:
            params = (order_detail.order_id, order_detail.product.id, order_detail.total)
            cursor = self.cursor.execute(SQL, params)
            self.conn.commit()
            order_detail.id = cursor.lastrowid
            return order_detail
        except Exception as error:
            print(error)
            return None

    def order_detail_update(self, order_detail: OrderDetail):
        """
        Update order detail
        :param order_detail: OrderDetail
        :param order_id: order id
        :return: updated OrderDetail
        """

        SQL = 'UPDATE order_detail SET orders_id=?, product_id=?, total=? ' \
              'WHERE id=?'
        params = (order_detail.order_id, order_detail.product.id, order_detail.total,
                  order_detail.id)
        try:
            self.cursor.execute(SQL, params)
            self.conn.commit()
            return order_detail
        except Exception as error:
            print(error)
            return None

    def order_detail_delete(self, id):
        """
        delete order detail
        :param id: order detail id
        :return: None
        """

        SQL = 'Delete FROM order_detail WHERE id=?'
        params = (id, )
        try:
            self.cursor.execute(SQL, params)
            self.conn.commit()
        except Exception as error:
            print(error)

    def order_detail_delete_all(self, order_id):
        """
        delete order details by order id
        :param id: order detail id
        :return: None
        """

        SQL = 'Delete FROM order_detail WHERE orders_id=?'
        params = (order_id, )
        try:
            row = self.cursor.execute(SQL, params)
            self.conn.commit()
            print(f"{row.rowcount} buyurtma detali o'chirildi")
            return row.rowcount > 0
        except Exception as error:
            print(error)
            return False

    def order_detail_get(self, id):
        """
        get order detail
        :param id: order detail id
        :return: OrderDetail
        """

        SQL = """
        SELECT o.orders_id, o.total, p.id,p.name,p.deadline,p.price,p.date_added,o.id
        FROM order_detail o
        LEFT JOIN product p on p.id = o.product_id
        WHERE o.id=?"""
        params = (id, )
        try:
            self.cursor.execute(SQL, params)
            row = self.cursor.fetchone()
            if not row:
                return None
            product = Product(id=row[2], name=row[3], deadline=date.fromisoformat(row[4]),
                              price=row[5], date_added=date.fromisoformat(row[6]))
            order_detail = OrderDetail(order_id=row[0], product=product, total=row[1], id=row[7])
            return order_detail

        except Exception as error:
            print(error)
            return None

    def order_detail_list(self, order_id):
        """
        Get order details by order id
        :param order_id: order id
        :return: list[OrderDetail]
        """

        SQL = """
        SELECT o.orders_id, o.total, p.id,p.name,p.deadline,p.price,p.date_added,o.id
        FROM order_detail o
        LEFT JOIN product p on p.id = o.product_id
        WHERE o.orders_id=?"""
        params = (order_id, )
        try:
            self.cursor.execute(SQL, params)
            rows = self.cursor.fetchall()
            if not rows:
                return None
            order_details = []
            for row in rows:
                product = Product(id=row[2], name=row[3], deadline=date.fromisoformat(row[4]),
                                  price=row[5], date_added=date.fromisoformat(row[6]))
                order_detail = OrderDetail(order_id=row[0], product=product, total=row[1], id=row[7])
                order_details.append(order_detail)
            return order_details

        except Exception as error:
            print(error)
            return []

    def order_insert(self, order: Orders):
        '''
        Buyurtmani kiritish yoki o'zgartirish uchun
        :return: OrderDetail
        '''

        SQL = 'INSERT INTO orders(client_id, created, status) ' \
              'VALUES(?,?,False)'
        params = (order.client.id, datetime.now())

        try:
            row = self.cursor.execute(SQL, params)
            order.id = row.lastrowid
            for order_detail in order.order_details:
                if not self.order_detail_insert(order_detail):
                    self.conn.rollback()
                    print('Xatolik')
                    return None
            self.conn.commit()
            print(f"Buyurtma id={order.id} kiritildi")
            return order
        except Exception as error:
            self.conn.rollback()
            print(error)
            return None

    def order_get(self, id):
        '''
        Buyurtmani o'qish uchun
        :return: Orders
        '''

        SQL = 'SELECT id,created,client_id,status ' \
              'FROM orders ' \
              'WHERE id=?'
        params = (id,)

        try:
            self.cursor.execute(SQL, params)
            row = self.cursor.fetchone()
            if not row:
                return None
            client = self.client_get(row[2])
            order_details = db.order_detail_list(row[0])
            order = Orders(id=row[0], client=client,
                           added_date=datetime.fromisoformat(row[1]),
                           order_details=order_details,
                           status=row[3])
            return order
        except Exception as error:
            print(error)
            return None

    def order_update(self, order: Orders):
        """
        Update order
        :param order:
        :return: updated Order
        """

        SQL = 'UPDATE orders SET created=?, client_id=?,status=? ' \
              'WHERE id=?'
        params = (order.added_date, order.client.id, order.status, order.id)

        try:
            row = self.cursor.execute(SQL, params)
            self.conn.commit()
            if row.rowcount > 0:
                return order
            else:
                return None
        except Exception as error:
            self.conn.rollback()
            print(error)
            return None

    def order_delete(self, id):
        """
        Delete order
        :param id:
        :return:
        """

        SQL = 'DELETE FROM orders ' \
              'WHERE id=?'
        params = (id, )

        try:
            row = self.cursor.execute(SQL, params)
            self.order_detail_delete_all(order_id=id)
            return row.rowcount > 0
        except Exception as error:
            print(error)
            return False


if __name__ == "__main__":
    db = DbManager()

    # PRODUCT
    # product = Product(name='sf', deadline=date(2023, 4, 12), price=3000, date_added=date.today())
    # print(product)
    # product = db.product_insert(product)
    # print(product)
    # product.name = '-------------'
    # db.product_update(product)
    # print(product)
    # db.product_delete(1000)
    # print(db.product_get(13))
    # for product in db.product_all():
    #     print(product)

    # CLIENT
    # row=db.client_insert(Client(name='-----',address='Yunusobod',birth_date=date(1982,1,1)))
    # print(row)
    # for client in db.client_all():
    #     print(client)
    # print(db.client_get(7))
    # client = Client(id=7, name="____")
    # clent = db.client_update(client)
    # print(clent)
    # db.client_delete(6)

    # == ORDER_DETAIL ==
    # GET
    # order_detail = db.order_detail_get(8)
    # order_detail.total = 25
    # order_detail.product.id = 13
    # UPDATE
    # order_detail = db.order_detail_update(order_detail)
    # DELETE
    # db.order_detail_delete(8)
    # INSERT
    # order_detail = db.order_detail_get(7)
    # order_detail.total = 100
    # db.order_detail_insert(order_detail)
    # LIST
    # for order_detail in db.order_detail_list(3):
    #     print(order_detail)

    # ORDER

    # INSERT
    # client = db.client_get(13)
    # banan = db.product_get(13)
    # olma = db.product_get(15)
    # order_details = [
    #     OrderDetail(product=banan, total=1, order_id=5),
    #     OrderDetail(product=olma, total=5, order_id=5),
    #     ]
    # order = Orders(client=client, order_details=order_details)
    # order = db.order_insert(order)

    # GET
    # order = db.order_get(5)
    # print(order)

    # UPDATE
    # order = db.order_get(15)
    # if order:
    #     order.status = True
    #     order = db.order_update(order)
    #     print(order)

    # DELETE

    # db.order_delete(2)
