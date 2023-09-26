from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user
from .models import Bike, Borrow_Session, Member


queries = Blueprint("queries", __name__)

@queries.route("/member_queries", methods=["GET", "POST"])
def member_queries():
    if not current_user.is_authenticated:
        flash("You need to be logged in to view this content.")
        return redirect(url_for("login"))
    
    filter_option = request.args.get("filter_option", "who-has-your-bikes")
    filtered_bikes = []

    if filter_option == "who-has-your-bikes":
        user_bikes = Bike.query.filter_by(owner_id=current_user.id).all()
        bike_ids = [bike.id for bike in user_bikes]
        borrow_sessions = (
            Borrow_Session.query
            .join(Member, Borrow_Session.borrower_id == Member.id)
            .add_columns(Member.email, Member.first_name)
            .filter(Borrow_Session.bike_id.in_(bike_ids))
            .all()
        )
        for session, borrower_email, borrower_name in borrow_sessions:
            filtered_bikes.append(f"Bike ID: {session.bike_id} | Borrower Name: {borrower_name} | Borrower Email:{borrower_email}")
    
    elif filter_option == "enlisted-bikes":
        user_bikes = Bike.query.filter_by(owner_id=current_user.id).all()
        for bike in user_bikes:
            filtered_bikes.append(f"Manufacture: {bike.manufacture} | Type: {bike.type} | Frame Height: {bike.frame_height}")
    return render_template("member_queries.html", filtered_bikes=filtered_bikes)








# @queries.route("/get_borrow_sessions", methods=["GET"])
# def get_borrow_sessions():
#     if not current_user.is_authenticated:
#         return []
    
#     user_bikes = Bike.query.filter_by(owner_id=current_user.id).all()

#     bike_ids = [bike.id for bike in user_bikes]

#     borrow_sessions = (
#         Borrow_Session.query
#         .join(Member, Borrow_Session.borrower_id == Member.id)
#         .add_columns(Member.email, Member.first_name)
#         .filter(Borrow_Session.bike_id.in_(bike_ids))
#         .all()
#     )
#     return borrow_sessions
    

# @queries.route("/my_bikes", methods=["GET"])
# def my_bikes():
#     if not current_user.is_authenticated:
#         return []
#     user_bikes = Bike.query.filter_by(owner_id=current_user.id).all()
#     return user_bikes
    