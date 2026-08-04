from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship
from datetime import datetime
from src.database import db



class Order(db.Model):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    delivery_id = Column(Integer, ForeignKey('deliveries.delivery_id'), nullable=False)
    total_price = Column(Float, nullable=False)
    status = Column(String(50), default='Pending')
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship('User')
    delivery = relationship('Delivery')

    def __repr__(self):
        return f'<Order {self.order_id} - User {self.user_id}>'
