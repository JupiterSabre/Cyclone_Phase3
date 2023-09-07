from flask import Blueprint, render_template, request, flash
from flask_login import current_user
from .models import Bike, Borrow_Session, Member


queries = Blueprint("queries", __name__)

@queries.route("/get_borrow_sessions", methods=["GET"])
def get_borrow_sessions():
    if not current_user.is_authenticated:
        return []
    
    user_bikes = Bike.query.filter_by(owner_id=current_user.id).all()

    bike_ids = [bike.id for bike in user_bikes]

    borrow_sessions = (
        Borrow_Session.query
        .join(Member, Borrow_Session.borrower_id == Member.id)
        .add_columns(Member.email, Member.first_name)
        .filter(Borrow_Session.bike_id.in_(bike_ids))
        .all()
    )
    return borrow_sessions
    
