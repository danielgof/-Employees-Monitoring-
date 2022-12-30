from sqlalchemy import Column, ForeignKey, String, Integer, Table
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
people_phones_association = Table(
    'people_phones', Base.metadata,
    Column('people_id', Integer, ForeignKey('people.id', ondelete='CASCADE',
     onupdate='CASCADE')),
    Column('phone_id', Integer, ForeignKey('phone.id', ondelete='CASCADE',
     onupdate='CASCADE'))
)

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