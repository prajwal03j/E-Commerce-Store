from backend.database.db import get_db

def get_all_products():
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    db.close()
    return products