from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from src.database import db





class Food(db.Model):
    __tablename__ = 'food_items'

    food_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String(255))
    image = Column(String(255))  # URL or image name
    category_id = Column(Integer, ForeignKey('categories.category_id'), nullable=False)


    # it’s creating a relationship between two tables in your database using SQLAlchemy's ORM.
    category = relationship('Category')

    def __repr__(self):
        return f'<Food {self.name}>'
