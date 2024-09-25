
from flask import Blueprint, jsonify, request

from postgres_proj.services.worker import get_all_users, insert_new_user

worker_bp = Blueprint("worker", __name__)

@worker_bp.route('/insert', methods=['POST'])
def insert_user():
    data = request.get_json()
    result = insert_new_user(data)
    if result is True:
        return jsonify({"result": result}), 201
    else:
        return jsonify({"result": result}), 400


@worker_bp.route('/find', methods=['GET'])
def find_all():
    data = request.args
    find_by = data.get('find_by')
    value = data.get('value')
    count = data.get('count')
    result, users = get_all_users(find_by=find_by, value=value, count=count)
    if result is True:
        return jsonify({"users": users}), 200
    else:
        return jsonify({"result": result}), 400



