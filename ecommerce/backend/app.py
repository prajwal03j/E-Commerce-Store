from flask import Flask, render_template, request, redirect, jsonify
import mysql.connector
from config import DB_CONFIG

app = Flask(__name__)

# ✅ DB CONNECTION
def get_db():
    return mysql.connector.connect(**DB_CONFIG)


# =========================
# HOME
# =========================
@app.route('/')
def home():
    return render_template('index.html')


# =========================
# REGISTER
# =========================
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        db = get_db()
        cursor = db.cursor()

        cursor.execute(
            "INSERT INTO users (email, password) VALUES (%s, %s)",
            (email, password)
        )

        db.commit()
        cursor.close()
        db.close()

        return redirect('/login')

    return render_template('register.html')


# =========================
# LOGIN
# =========================
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        db = get_db()
        cursor = db.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM users WHERE email=%s",
            (email,)
        )

        user = cursor.fetchone()

        cursor.close()
        db.close()

        if user and user['password'] == password:
            return redirect('/')

        return "Login Failed ❌"

    return render_template('login.html')


# =========================
# PRODUCTS API (IMPORTANT)
# =========================
@app.route('/products')
def products():
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT name, price FROM products")
    rows = cursor.fetchall()

    data = []
    for row in rows:
        data.append({
            "name": row[0],
            "price": row[1]
        })

    cursor.close()
    db.close()

    return jsonify(data)


# =========================
# CART PAGE
# =========================
@app.route('/cart')
def cart():
    return render_template('cart.html')


# =========================
# ORDERS PAGE
# =========================
@app.route('/orders')
def orders():
    return render_template('orders.html')


# =========================
# RUN
# =========================
if __name__ == "__main__":
    print("🚀 Server running at http://127.0.0.1:5000")
    app.run(debug=True)