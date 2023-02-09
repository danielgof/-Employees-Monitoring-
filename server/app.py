from flask import Flask, request, jsonify, abort, Response
from flask_cors import CORS
import logging
import os
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date

from api.main_api import main_controller
from api.person_api import person_controller
from api.phone_api import phone_controller
from api.position_api import position_controller


app = Flask(__name__)
app.register_blueprint(main_controller)
app.register_blueprint(person_controller)
app.register_blueprint(phone_controller)
app.register_blueprint(position_controller)
CORS(app)

if not os.path.isdir("./log"):
    os.mkdir("./log")
logging.basicConfig(filename=f'./log/{date.today()}.log', level=logging.DEBUG)

if __name__ == "__main__":
    app.run(port = 5000, debug = True)