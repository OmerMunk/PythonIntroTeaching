from crypt import methods

from flask import Blueprint, request, jsonify
from ..services.todo import create_todo as insert_todo



todos_bp = Blueprint('todos', __name__, url_prefix='/todos')



@todos_bp.route('/', methods=['POST'])
def create_todo():
    data = request.get_json()
    result = insert_todo(data)
    if result.get('error'):
        return jsonify(result), 400
    return jsonify(result), 201


