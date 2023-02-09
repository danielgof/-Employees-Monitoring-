from flask import Blueprint, request, jsonify, abort, Response
from datetime import datetime
from flask import current_app

from create import *
from models.people import *
from models.phones import *
from models.positions import *


main_controller = Blueprint("main", __name__)
"""
main api
"""
@main_controller.route("/api/v1/num_visits", methods=["GET"])
def num_visits():
    count = get_hit_counts()
    current_app.logger.info(f"Number of visitors of portal at {datetime.today().strftime('%Y-%m-%d')} is {count}")
    return jsonify({"visited": count})


@main_controller.route("/api/v1/get_all_people_data", methods=["GET"])
def get_all_data():    
    try:
        data = session.query(Person).all()
        res = list()
        for person in data:
            all_phones = []
            phone_num = session.query(Phone) \
            .join(Phone, Person.phones) \
            .filter(Person.id == person.id) \
            .all()
            for phone in phone_num:
                all_phones.append(phone.phone)
            position = session.query(Positon).filter(Positon.id == person.position_id).first()
            if position == None:
                continue
            if phone_num == None:
                continue
            res.append({
            "id": person.id,
            "position": position.position,
            "last_name": person.last_name,
            "first_name": person.first_name,
            "salary": position.salary,
            "department": position.departament,
            "phone": all_phones
            })
        current_app.logger.info("All users were selected from database")
        return res 
    except Exception as e:
        current_app.logger.warning(f"Exeption {e} ocured")
        abort(Response(e, 500))


@main_controller.route("/api/v1/get_all_positions", methods=["GET"])
def positions_info():
    try:
        data = session.query(Positon).all()
        res = list()
        for position in data:
            res.append({
            "id":position.id,
            "position": position.position,
            "salary": position.salary,
            "department": position.departament
            })
        current_app.logger.info("All users were selected from database")
        return res 
    except Exception as e:
        current_app.logger.warning(f"Exeption {e} ocured")
        abort(Response(e, 500))