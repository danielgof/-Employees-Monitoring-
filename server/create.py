from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import date

import models.people
import models.phones
import models.positions
from utils import *
from base import *

db_username, db_password, db_name, = get_configs()
engine = create_engine(f"postgresql://{db_username}:{db_password}@localhost:5432/{db_name}")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
