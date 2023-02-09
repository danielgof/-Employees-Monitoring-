from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship
from models.phones import *
from base import *

"""People"""
class Person(Base):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True)
    last_name = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    position_id = Column(Integer, ForeignKey("position.id", ondelete='CASCADE'))
    phones = relationship("Phone", secondary=people_phones_association)

    def __init__(self, last_name, first_name, position_id):
        self.last_name = last_name
        self.first_name = first_name
        self.position_id = position_id