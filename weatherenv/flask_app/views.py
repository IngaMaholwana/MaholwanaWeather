from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def weatherhomepage():
    """when even the slash is ran this will go to the home page"""
    return render_template("weather.html")