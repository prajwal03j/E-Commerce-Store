import mysql.connector

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",          # change if using grocery_user
        password="1234",      # your MySQL password
        database="grocery_store"
    )