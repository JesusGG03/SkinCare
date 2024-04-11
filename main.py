import mysql.connector
from config import Credentials
import database
from DisplayProducts import displayProducts


db = database.connection
print()

if __name__ == "__main__":
    display_products = displayProducts()

    user_input = input("Enter skin care categories(seperate by comma): ").strip().split(",")
    categories = [category.strip() for category in user_input]
    display_products.display_products(categories)