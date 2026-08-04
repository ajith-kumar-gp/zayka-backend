from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.database import db


class Delivery(db.Model):
    __tablename__ = 'deliveries'

    delivery_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    address_line = Column(String(255), nullable=False)
    city = Column(String(100), nullable=False)
    pincode = Column(String(20), nullable=False)
    phone_number = Column(String(15), nullable=False)

    user = relationship('User')

    def __repr__(self):
        return f'<Delivery {self.address_line}, {self.city}>'
