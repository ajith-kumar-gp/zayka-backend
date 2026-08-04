from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.sql import func
from src.database import db


# enumeration for user roles
# This can be extended to include more roles as needed.
class User_Role:
    admin = "Admin"
    user = "User"



class User(db.Model):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)  # Required
    email = Column(String(120), unique=True, nullable=False)  # Required & unique
    password = Column(String(255), nullable=False)  # Required
    cartdata = Column(JSON, default={})  # Object type with default {}
    user_role = Column(String(50), nullable = False, default=User_Role.user)  # Default user roll is 'User'


    def __repr__(self):
        return f'<User {self.username}>'
        # returns = <User noor> if used with __repr__




