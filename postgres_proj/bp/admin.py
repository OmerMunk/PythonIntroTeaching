
from flask import Blueprint, jsonify, request

from postgres_proj.services.admin import create_users_table, alter_users_table, create_payments_table

admin_bp = Blueprint("admin", __name__)

@admin_bp.route('/create/<str:table>', methods=['POST'])
def create_table(table):
    request_info = {
        "ip": request.remote_addr,
        "endpoint": request.url,
        "method": request.method
    }
    if table == "users":
        result = create_users_table(request_info)
    elif table == "payments":
        result = create_payments_table(request_info)

    if result:
        return jsonify({"result": result}), 201
    else:
        return jsonify({"result": result}), 400




@admin_bp.route('/alter', methods=['POST'])
def alter_table():
    request_info = {
        "ip": request.remote_addr,
        "endpoint": request.url,
        "method": request.method
    }
    result = alter_users_table(request_info)
    if result is True:
        return jsonify({"result": result}), 200
    else:
        return jsonify({"result": result}), 400





