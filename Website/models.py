#  ( . ) refers to current package (website)
# flask_login is module for logins

from flask_login import UserMixin
from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


class User(db.Model, UserMixin, SerializerMixin):
    ___tablname__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String(150), nullable=False)

    
    # Set up relationships
    queries = db.relationship('Query', back_populates = 'user')
    
    # Associations
    medications = association_proxy('queries', 'medication')

    # Serialize Rules
    serialize_rules = ('-queries.user',)



class Medication (db.Model, SerializerMixin):
    __tablename__ = 'medications'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    generic_name = db.Column(db.String(80))
    brand_name = db.Column(db.String(80))
    known_interactions = db.Column(db.String(2000))


    # Set up relationships
    queries = db.relationship('Query', back_populates = 'medication')

    # Associations
    users = association_proxy('queries', 'user')


    # Serialize Rules
    serialize_rules = ('-queries.medication',)



class Query (db.Model, SerializerMixin, UserMixin):
    __tablename__ = "queries"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    generic_name = db.Column(db.Column(45))

    # Foreign Keys
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    medication_id = db.Column(db.Integer, db.ForeignKey("medications.id"))

    # Set up relationships
    user = db.relationship("User", back_populates = 'queries')
    medication = db.relationship("Medication", back_populates = 'queries')

    # Serialize Rules
    serialize_rules = ('-user.queries', '-medication.queries')


    

    
    



