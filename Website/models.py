#  ( . ) refers to current package (website)
# flask_login is module for logins
from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy



class User(db.Model, UserMixin, SerializerMixin):
    # ___tablname__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String(150), nullable=False)

    
    # Set up relationships
    basemeds = db.relationship("BaseMedication", back_populates = 'user')
    
    # Associations
    comparisonmedications = association_proxy('basemedications', 'comparisonmedication')

    # Serialize Rules
    serialize_rules = ('-basemedications.user')



class BaseMedication (db.Model, SerializerMixin, UserMixin):
    __tablename__ = "base_medications"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    generic_name = db.Column(db.Column(45))
    manufacturer = db.Column(db.String(45))
    known_interactions = db.Column(db.Column(80))


    # Foreign Keys
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    comparison_medication_id = db.Column(db.Integer, db.ForeignKey("comparison_medications.id"))

    # Set up relationships
    user = db.relationship("User", back_populates = 'basemedications')
    comparisonmedication = db.relationship("ComparisonMedication", back_populates = 'basemedication')

    # Serialize Rules
    serialize_rules = ('-user.basemedications', '-comparisonmedications.basemedications')


    
class ComparisonMedication (db.Model, SerializerMixin):
    __tablenames__ = "comparison_medications"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    generic_name = db.Column(db.String(45))
    manufacturer = db.Column(db.String(45))

    # Set up relationships
    basemedications = db.relationship("BaseMedication", back_populates = 'comparisonmedication')

    # Associations
    users = association_proxy('basemedications', 'user')


    # Serialize Rules
    serialize_rules = ('-basemedications.comparisonmedications')


    
    



