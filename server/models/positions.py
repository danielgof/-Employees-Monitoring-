from sqlalchemy import Column, String, Integer
from base import *

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
