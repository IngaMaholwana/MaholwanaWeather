from flask import Blueprint, render_template
from flask_login import login_required, current_user
views = Blueprint('views', __name__)

@views.route('/')
@login_required
def weatherhomepage():
    """when even the slash is ran this will go to the home page"""
    return render_template("weather.html")