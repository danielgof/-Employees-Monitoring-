from sqlalchemy import Column, ForeignKey, String, Integer, Table
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from models.utils import *
username, password, dbname = get_configs()
engine = create_engine(f"postgresql://{username}:{password}@localhost:5432/{dbname}")
Session = sessionmaker(bind=engine)
print("session created succesfully")

"""Create a base class"""
Base = declarative_base()
"""Tables"""
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


Base.metadata.create_all(engine)

# CEO = Positon("all", "1000000", "CEO")
# CTO = Positon("all", "650000", "CTO")
# SE = Positon("Cloud storage", "250000", "SE")
# CAE = Positon("Audit", "350000", "CAE")
# Auditor = Positon("Audit", "150000", "Auditor")
# CAIO = Positon("Artificial Intelligence", "400000", "CAIO")
# DS = Positon("Artificial Intelligence", "200000", "DS")


# Richard = Person("Handrix", "Richard", 1)
# Jared = Person("Dunn", "Jared", 2)
# Dinesh = Person("Chuktai", "Dinesh", 3)
# Gilfoyel = Person("Burtram", "Gilfoyel", 3)
# Neil = Person("Thompson", "Neil", 4)
# Jose = Person("Chavez", "Jose", 5)
# Hector = Person("Woods", "Hector", 5)
# William = Person("Neal", "William", 6)
# Ralph = Person("Clark", "Ralph", 7)
# Eugene = Person("Powell", "Eugene", 7)
# Leon = Person("Martinez", "Leon", 3)
# Carl = Person("Wallace", "Carl", 5)

# Richard_phone = Phone("3459875667")
# Jared_phone = Phone("3454568976")
# Dinesh_phone = Phone("7652346787")
# Gilfoyel_phone = Phone("9875675465")
# Neil_phone = Phone("9349875667")
# Jose_phone = Phone("1357468976")
# Hector_phone = Phone("7652376487")
# William_phone = Phone("9898775465")
# Ralph_phone = Phone("3454568064")
# Eugene_phone = Phone("4552348787")
# Leon_phone = Phone("9887775465")
# Carl_phone = Phone("3459983467")


# Richard.phones = [Richard_phone]
# Jared.phones = [Jared_phone]
# Dinesh.phones = [Dinesh_phone]
# Gilfoyel.phones = [Gilfoyel_phone]
# Neil.phones = [Neil_phone] 
# Jose.phones = [Jose_phone]
# Hector.phones = [Hector_phone]
# William.phones = [William_phone]
# Ralph.phones = [Ralph_phone]
# Eugene.phones = [Eugene_phone]
# Leon.phones = [Leon_phone] 
# Carl.phones = [Carl_phone]

# session = Session()
# session.add(CEO)
# session.add(CTO)
# session.add(SE)
# session.add(CAE)
# session.add(Auditor)
# session.add(CAIO)
# session.add(DS)

# session.commit()
# session.close()

# session.add(Richard)
# session.add(Jared)
# session.add(Dinesh)
# session.add(Gilfoyel)
# session.add(Neil)
# session.add(Jose)
# session.add(Hector)
# session.add(William)
# session.add(Ralph)
# session.add(Eugene)
# session.add(Leon)
# session.add(Carl)

# session.commit()
# session.close()

# session.add(Richard_phone )
# session.add(Jared_phone )
# session.add(Dinesh_phone )
# session.add(Gilfoyel_phone )
# session.add(Neil_phone)
# session.add(Jose_phone)
# session.add(Hector_phone)
# session.add(William_phone)
# session.add(Ralph_phone)
# session.add(Eugene_phone)
# session.add(Leon_phone)
# session.add(Carl_phone)

# session.commit()
# session.close()