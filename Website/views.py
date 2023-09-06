# Store standard roots for your website (main directory)
from flask import Blueprint, render_template, request
from flask_login import login_required, current_user




views = Blueprint("views", __name__)



@views.route("/", methods=["GET", "POST"])
@login_required #Assured you cannot access homepage without being logged in.
def home():
    if request.method == "POST":
        new_bike = request.form.get("bike")
        

    return render_template("home.html", member=current_user)