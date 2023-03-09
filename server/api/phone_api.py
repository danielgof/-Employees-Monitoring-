from flask import Blueprint, request, jsonify, abort
from create import *
from models.people import *
from models.phones import *
from models.positions import *

phone_controller = Blueprint("phone", __name__, url_prefix="/api/v1")


@phone_controller.route("/upd_phone", methods=["PUT"])
def upd_phone():
    data = request.get_json(force=True)
    phone = session.query(Phone)\
    .filter(Phone.phone == data["phonenumber_old"])\
    .update({Phone.phone: data["phonenumber_new"]}, synchronize_session = False)
    session.commit()
    return jsonify({"result":"success"})


@phone_controller.route("/delete_phone", methods=["DELETE"])
def delete_phone():
    data = request.get_json(force=True)
    session.query(Phone).filter(Phone.phone == data["phone"]).delete()
    session.commit()
    return jsonify({"result":"success"})


@phone_controller.route("/add_phone_to_user", methods=["POST"])
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