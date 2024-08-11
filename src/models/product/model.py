from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, ForeignKey, Float, Numeric, Date, BigInteger
from sqlalchemy.orm import relationship

from src.db.database import Base


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, index=True, nullable=False)
    status = Column(Boolean, default=True)
    create_at = Column(TIMESTAMP, default=datetime.now())
    update_at = Column(TIMESTAMP, default=datetime.now())

    sub_category = relationship("Sub_Category", back_populates="category")
    
class Sub_Category(Base):
    __tablename__ = "sub_category"

    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey("category.id", ondelete="SET NULL"))
    name = Column(String(50), unique=True, index=True, nullable=False)
    status = Column(Boolean, default=True)
    create_at = Column(TIMESTAMP, default=datetime.now())
    update_at = Column(TIMESTAMP, default=datetime.now())

    category = relationship("Category", back_populates="sub_category")
    product = relationship("Product", back_populates="sub_category")
    

class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    sub_category_id = Column(Integer, ForeignKey("sub_category.id", ondelete="SET NULL"))
    name = Column(String(250), index=True, nullable=False)
    
    sub_category = relationship("Sub_Category", back_populates="product")