
from flask import Blueprint, jsonify, request

from postgres_proj.services.admin import create_users_table

admin_bp = Blueprint("admin", __name__)

@admin_bp.route('/create', methods=['POST'])
def create_table():
    result = create_users_table()
    if result is True:
        return jsonify({"result": result}), 201
    else:
        return jsonify({"result": result}), 400


