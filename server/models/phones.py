from sqlalchemy import Column, ForeignKey, String, Integer, Table
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

"""Phones"""
class Phone(Base):
    __tablename__ = "phone"
    id = Column(Integer, primary_key=True)
    phone = Column(String, nullable=False, index=True, unique=True)

    def __init__(self, phone):
        self.phone = phone
