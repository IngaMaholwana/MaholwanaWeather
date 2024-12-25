from flask import Blueprint,render_template, request, flash, redirect,url_for
from werkzeug.security import generate_password_hash, check_password_hash   
from .models import User
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    """this is the main page for the login and will be routing here """
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('logged in successfully', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.weatherhomepage'))
            else:
                flash('incorrect password', category='error')
        else:
            flash('email does not exist', category='error') 
    return render_template("login.html")

@auth.route('/logout')
@login_required
def logout():
    """this is the main page for the logout and will be routing here to the login and log out the session of the user """
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    """this is the main page for the signup and will be routing here #jonga lewii ifuna la hyphan phakathi kwazo"""
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('email already exists', category='error')

        elif len(email) < 4:
            flash('email must be greater than 3 characters long',category='error')
            
        elif len(firstName) < 2:
            flash('name must be greater than 1 character long',category='error')
            
        elif password1 != password2:
            flash('try again password dont match',category='error')
            
        elif len(password1) < 7:
            flash('email must be greater than 7 characters long',category='error')
            
        else:
            new_user = User(email=email, first_name=firstName, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('account created welcome')
            
            return redirect(url_for('views.weatherhomepage'))


    return render_template("signup.html")