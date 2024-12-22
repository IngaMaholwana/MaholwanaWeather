from flask import Flask, render_template, redirect, url_for, flash,request

app = Flask(__name__)
app.secret_key = 'move_me_when_all_of_this_is_done'  # For securely flashing messages

# Temporary storage for user accounts (use a database in production)
users = {}

# @app.route('/')
# def home():
#     return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']

        # Validate user
        if username in users and users[username] == password:
            flash("Login successful!", "success")
            return redirect(url_for('welcome', username=username))
        else:
            flash("Invalid username or password.", "danger")
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        password_repeat = request.form['password-repeat']

        # Check if passwords match
        if password != password_repeat:
            flash("Passwords do not match!", "danger")
        elif email in users:
            flash("User already exists!", "warning")
        else:
            # Store user
            users[email] = password
            flash("Account created successfully! Please log in.", "success")
            return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/welcome/<username>')
def welcome(username):
    return f"<h1>Welcome, {username}!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
