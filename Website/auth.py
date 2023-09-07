from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from .models import Member
from .queries import get_borrow_sessions
from . import db

# hashing functions are functions that have no inverse, use for beefing up password security. sha256 is a hasing algorithm. There are others if you have another preference.
from werkzeug.security import generate_password_hash, check_password_hash

# __name__ is a parameter argument to the 
auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        member = Member.query.filter_by(email=email).first()
        if member:
            if check_password_hash(member.password, password):
                flash("Login Success. Welcome to the circle of trust 🙏🏽", category="success")
                login_user(member, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Incorrect password, try again", category="error")
        else:
            flash("Email not in registry", category="error")
    return render_template("login.html", member=current_user)


# @auth




@auth.route("/logout")
@login_required # This decorator assures that you cannot logout without being logged in.
def logout():
    logout_user()
    return redirect(url_for("auth.login"))




@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        first_name = request.form.get("first_name")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        member = Member.query.filter_by(email=email).first()
        if member:
            flash("This email is already registered", category="error")

        elif len(email) < 4 :
            flash("Email must be greater than 3 characters", category="error")

        elif len(first_name) < 2 :
            flash("First name must be greater than 1 character", category="error")

        elif password1 != password2:
            flash("Passwords don't match", category="error")

        elif len(password1) < 7:
            flash("Password must be at least 8 characters", category="error")

        else:
            new_member = Member(email=email, first_name=first_name, password=generate_password_hash(password1, method="sha256"))
            db.session.add(new_member)
            db.session.commit()
            login_user(member, remember=True)
            flash("Account created!", category="success")
            return redirect(url_for("views.home"))

    return render_template("sign-up.html", member=current_user)

