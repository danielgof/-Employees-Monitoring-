from sqlalchemy import Column, ForeignKey, String, Integer, Table
from base import *

"""Phones"""
class Phone(Base):
    __tablename__ = "phone"
    id = Column(Integer, primary_key=True)
    phone = Column(String, nullable=False, index=True, unique=True)

    def __init__(self, phone):
        self.phone = phone


people_phones_association = Table(
    'people_phones', Base.metadata,
    Column('people_id', Integer, ForeignKey('people.id', ondelete='CASCADE',
     onupdate='CASCADE')),
    Column('phone_id', Integer, ForeignKey('phone.id', ondelete='CASCADE',
     onupdate='CASCADE'))
)
