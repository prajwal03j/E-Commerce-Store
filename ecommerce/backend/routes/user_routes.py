from flask import Blueprint, render_template, request, redirect, session
from backend.models.user_model import create_user, get_user

user_bp = Blueprint('user', __name__)

# ✅ REGISTER
@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        create_user(email, password)
        return redirect('/login')

    return render_template('register.html')


# ✅ LOGIN
@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = get_user(email)

        if user and user['password'] == password:
            session['user_id'] = user['id']
            return redirect('/products')

        return "Login Failed ❌"

    return render_template('login.html')