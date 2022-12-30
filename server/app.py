from flask import Flask, request, jsonify, abort, Response
from flask_cors import CORS
# import redis
# import logging
# import os
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.utils import *
from models.db import *
from api.main_controller import main_controller
from api.person_controller import person_controller
from api.phone_controller import phone_controller
from api.position_controller import position_controller

# username, password, dbname = get_configs()
# engine = create_engine(f"postgresql://{username}:{password}@localhost:5432/{dbname}")
app = Flask(__name__)
app.register_blueprint(main_controller)
app.register_blueprint(person_controller)
app.register_blueprint(phone_controller)
app.register_blueprint(position_controller)
CORS(app)


if __name__ == "__main__":
    app.run(port = 5000, debug = True)