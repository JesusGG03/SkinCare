import mysql.connector
from config import Credentials

error = mysql.connector.Error


class queryProduct:
    def __init__(self):
        self.db_connection = mysql.connector.connect(**Credentials.credentials)
        self.cursor = self.db_connection.cursor()

    def format_display(self, product):
        productID, brand, name, price = product
        productID = str(productID).strip("'")
        brand = brand.strip("'")
        name = name.strip("'")
        price = str(price).strip("Decimal('").strip("')")

        formatted = f"{productID}, {brand}, {name.ljust(70, '.')} {price}"
        return formatted


    def fetch_products(self, category):
        try:
            self.cursor.execute("SHOW TABLES")
            tables = [table[0] for table in self.cursor.fetchall()]
            if category not in tables:
                print(f"Category {category} is not available")
                return []

            self.cursor.execute(f"SELECT id, brand, name, price FROM {category}")
            products = self.cursor.fetchall()
            return products
        except error as e:
            print(f"Error retrieving {category}")
            return[]



class displayProducts:
    def __init__(self):
        self.query_product = queryProduct()

    def display_products(self, categories):
        for cateory in categories:
            products = self.query_product.fetch_products(cateory)
            print(f"{cateory}: ")
            for product in products:
                formatted_display = self.query_product.format_display(product)
                print(formatted_display)
                print()
