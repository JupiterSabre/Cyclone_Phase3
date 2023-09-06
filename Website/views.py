# Store standard roots for your website (main directory)
from flask import Blueprint, render_template


views = Blueprint("views", __name__)



@views.route("/")
def home():
    return render_template("home.html")