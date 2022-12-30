from flask import Blueprint, request, jsonify, abort, Response
from flask_cors import CORS
from datetime import date
from flask import current_app
import os
import logging
from models.db import *

Session = sessionmaker(bind=engine)
session = Session()
if not os.path.isdir("./log"):
    os.mkdir("./log")
logging.basicConfig(filename=f'./log/{date.today()}.log', level=logging.DEBUG)
phone_controller = Blueprint('phone', __name__)


@phone_controller.route("/api/v1/upd_phone", methods=["PUT"])
def upd_phone():
    data = request.get_json(force=True)
    phone = session.query(Phone)\
    .filter(Phone.phone == data["phonenumber_old"])\
    .update({Phone.phone: data["phonenumber_new"]}, synchronize_session = False)
    session.commit()
    return jsonify({"result":"success"})


@phone_controller.route("/api/v1/delete_phone", methods=["DELETE"])
def delete_phone():
    data = request.get_json(force=True)
    session.query(Phone).filter(Phone.phone == data["phone"]).delete()
    session.commit()
    return jsonify({"result":"success"})


@phone_controller.route("/api/v1/add_phone_to_user", methods=["POST"])
def add_phone_to_user():
    data = request.get_json(force=True)
    new_phones = []
    person = session.query(Person)\
    .filter(Person.id == data["id"])\
    .first()
    person_phones = session.query(Phone) \
    .join(Phone, Person.phones) \
    .filter(Person.id == person.id) \
    .all()
    for phone in person_phones:
        new_phones.append(phone)
    new_phone = Phone(data["phone"])
    new_phones.append(new_phone)
    person.phones = new_phones
    session.add(person)
    session.commit()
    return jsonify({"result": "success"})