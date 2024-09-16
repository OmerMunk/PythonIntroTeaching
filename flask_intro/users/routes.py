from flask import Blueprint, jsonify, request
from .models import User, db


users_bp = Blueprint('users', __name__)


@users_bp.route('/')
def home():
    return 'Welcome to the best Kodcode API ever!! Shkoyech'

@users_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'name': user.name, 'email': user.email, 'age': user.age} for user in users]), 200


@users_bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    # user = User.query.get(id) -> found nothing? return None
    user = User.query.get_or_404(id)
    print(type(user))
    return jsonify({'name': user.name, 'email': user.email, 'age': user.age}), 200
    # filtered = list(filter(lambda user: user['id'] == id, ))
    # if (len(filtered) == 1):
    #     return jsonify(filtered[0]), 200
    # else: #len = 0
    #     return jsonify({"error": f"user with the id {id} not exist"}), 404


@users_bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get(id)
    if user:
        data = request.get_json()
        if data.get('name'):
            user.name = data['name']
        if data.get('age'):
            user.age = data['age']
        db.session.commit()
        return jsonify({'name': user.name, 'age': user.age}), 200
    else:
        return jsonify({'message': 'user not found'}), 404

@users_bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'user deleted'}), 200




@users_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(name=data['name'], email=data['email'], password=data['password'], age=data['age'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({
        'message': 'user created',
        'user': {
            'id': new_user.id,
            'name': new_user.name,
        }

    }), 201


