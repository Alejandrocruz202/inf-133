from database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = "users"
    # Define las columnas de la tabla `users`
    id = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String(50), nullable=False)
    editorial =db.Column(db.String(50),nullable=False)
    
    
