from sqlalchemy import Column, Integer, String
from src.database import db




class Category(db.Model):
    __tablename__ = 'categories'

    category_id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)

    def __repr__(self):
        return f'<Category {self.name}>'
