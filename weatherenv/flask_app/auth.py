from flask import Blueprint,render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    """this is the main page for the login and will be routing here """
    data = request.form
    print(data)
    return render_template("login.html")

@auth.route('/logout')
def logout():
    """this is the main page for the logout and will be routing here """
    return "<p>Logout</p>"


@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    """this is the main page for the signup and will be routing here #jonga lewii ifuna la hyphan phakathi kwazo"""
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('email must be greater than 3 characters long',category='error')
            pass
        elif len(firstName) < 2:
            flash('name must be greater than 1 character long',category='error')
            pass
        elif password1 != password2:
            flash('try again password dont match',category='error')
            pass
        elif len(password1) < 7:
            flash('email must be greater than 7 characters long',category='error')
            pass
        else:
            flash('account created welcome')
            # add user to database
            pass


    return render_template("signup.html")