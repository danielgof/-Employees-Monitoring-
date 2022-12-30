from sqlalchemy import Column, ForeignKey, String, Integer, Table
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# from utils import *
# username, password, dbname = get_configs()
# engine = create_engine(f"postgresql://{username}:{password}@localhost:5432/{dbname}")
# Session = sessionmaker(bind=engine)

Base = declarative_base()
"""Positons"""
class Positon(Base):
    __tablename__ = "position"
    id = Column(Integer, primary_key=True)
    departament = Column(String, nullable=False)
    salary = Column(String, nullable=False)
    position = Column(String, nullable=False)

    def __init__(self, departament, salary, position):
        self.departament = departament
        self.salary = salary
        self.position = position
