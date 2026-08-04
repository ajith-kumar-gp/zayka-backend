# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import Column, Integer, String, Float, ForeignKey
# from datetime import datetime

# db = SQLAlchemy()

# class Cart(db.Model):
#     __tablename__ = 'cart'

#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, nullable=False)   # Link to your user table
#     food_id = Column(Integer, nullable=False)   # Link to your food table
#     food_name = Column(String(100), nullable=False)  # Store food name
#     image = Column(String(255))  # URL or image name
#     price = Column(Float, nullable=False)  # Store price at the time of adding to cart
#     quantity = Column(Integer, default=1)
#     created_at = Column(datetime, default=datetime.utcnow)