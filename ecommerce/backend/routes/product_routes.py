from flask import Blueprint, jsonify
from backend.database.db import get_db

product_bp = Blueprint('product', __name__)

@product_bp.route('/products')
def products():
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT name, price FROM products")
    rows = cursor.fetchall()

    products = []
    for row in rows:
        products.append({
            "name": row[0],
            "price": row[1]
        })

    cursor.close()
    db.close()

    return jsonify(products)   # ✅ IMPORTANT