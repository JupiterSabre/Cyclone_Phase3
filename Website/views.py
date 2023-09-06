# Store standard roots for your website (main directory)
from flask import Blueprint, render_template
from flask_login import login_required, current_user



views = Blueprint("views", __name__)



@views.route("/")
@login_required #Assured you cannot access homepage without being logged in.
def home():
    return render_template("home.html")