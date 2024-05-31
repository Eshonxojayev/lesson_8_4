from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean, Float
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType
from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(20), nullable=True)
    last_name = Column(String(20), nullable=True)
    username = Column(String(10), unique=True)
    email = Column(Text, nullable=True)
    password = Column(Text, nullable=True)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
    orders = relationship('Order', back_populates='users')

    def __repr__(self):
        return self.first_name

class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    product = relationship('Product', back_populates='category')

class Product(Base):

    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(Text)
    price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship('Category', back_populates='product')
    orders = relationship('Order', back_populates='product')


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    users = relationship('User', back_populates='orders')
    product = relationship('Product', back_populates='orders')