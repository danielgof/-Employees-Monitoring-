from flask import Blueprint, request, jsonify, abort, Response
from flask_cors import CORS
from datetime import date
from datetime import datetime, timedelta
from flask import current_app
import os
import logging
from models.db import *

Session = sessionmaker(bind=engine)
session = Session()
if not os.path.isdir("./log"):
    os.mkdir("./log")
logging.basicConfig(filename=f'./log/{date.today()}.log', level=logging.DEBUG)
position_controller = Blueprint('position', __name__)

@position_controller.route("/api/v1/add_position", methods=["POST"])
def add_position():
    data = request.get_json(force=True)
    position = Positon(
        data["departament"],
        data["salary"],
        data["position"]
    )
    session.add(position)
    session.commit()
    return jsonify({"result": "success"})


@position_controller.route("/api/v1/delete_position", methods=["DELETE"])
def delete_position():
    data = request.get_json(force=True)
    session.query(Positon).filter(Positon.id == data["id"]).delete()
    session.commit()
    return jsonify({"result": "success"})


@position_controller.route("/api/v1/upd_position_for_person", methods=["PUT"])
def upd_position_for_person():
    data = request.get_json(force=True)
    session.query(Person)\
    .filter(Person.id == data["id"])\
    .update({Person.position_id: data["position_new"]}, synchronize_session = False)
    session.commit()
    return jsonify({"result":"success"})


@position_controller.route("/api/v1/upd_position", methods=["PUT"])
def upd_position():
    data = request.get_json(force=True)
    session.query(Positon)\
    .filter(Positon.id == data["id"])\
    .update({
        Positon.departament: data["departament"], 
        Positon.salary: data["salary"],
        Positon.position: data["position"]
        }, synchronize_session = False)
    session.commit()
    return jsonify({"result":"success"})