#  ( . ) refers to current package (website)
# flask_login is module for logins
from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy


metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})


db = SQLAlchemy(metadata=metadata)


class Member(db.Model, UserMixin):
    ___tablname__ = "members"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String(150), nullable=False)
    bike_shop = db.Column(db.String(150))
    bikes_shared = db.relationship("Bike", backref="member")




class Bike(db.Model):
    __tablename__ = "bikes"
    id = db.Column(db.Integer, primary_key=True)
    manufacture = db.Column(db.String(45))
    type = db.Column(db.String(45))
    frame_height = db.Column(db.String(15))
    lock_combo = db.Column(db.String(100))
    date_registered = db.Column(db.String(15))


    owner_id = db.Column(db.Integer, db.ForeignKey("member.id"))
    current_borrow_status = db.Column(db.String(15))
    

    
class Borrow_Session (db.Model):
    __tablenames__ = "borrow-sessions"
    id = db.Column(db.Integer, primary_key=True)
    bike_owner_name = db.Column(db.String, db.ForeignKey("member.first_name"))
    bike_owner_email = db.Column(db.String, db.ForeignKey("member.email"))
    bike_id = db.Column(db.String, db.ForeignKey("bike.id"))
    borrower_id = db.Column(db.Integer, db.ForeignKey("member.id"))

    # RELATIONSHIPS #
    



