from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from markupsafe import escape
from flask_limiter import Limiter

from .models import User, db

users_bp = Blueprint('users', __name__)



@users_bp.route('/')
def home():
    return 'Welcome to the best Kodcode API ever!! Shkoyech'


admins = [
    {
        'username': 'admin1',
        'password': '123456'
    }
]


@users_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if username and password:
        found = list(filter(lambda admin: username == admin['username'] and password == admin['password'], admins))
        if found and len(found) == 1:
            access_token = create_access_token(identity=username)
            return jsonify({'access_token': access_token, 'message': 'login success'}), 200
        else:
            return jsonify({'message': 'login failed'}), 401


def generate_users_response(users=None, user=None):
    if users:
        return [{'name': user.name, 'email': user.email, 'age': user.age} for user in users]
    elif user:
        return {'name': user.name, 'email': user.email, 'age': user.age}


@users_bp.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    identity = get_jwt_identity()
    if identity == 'admin1':
        print(identity)
        users = User.query.all()
        users_response = generate_users_response(users=users)
        return jsonify(users_response), 200

@users_bp.route('/users/search', methods=['GET'])
def search_users():
    '/users/search?email=a@a.com'
    email = request.args.get('email') # a@a.com
    # parameterized query of sql alchemy to prevent sql injection
    user = User.query.filter_by(email=email).first()



@users_bp.route('/users/<int:id>', methods=['GET'])

def get_user(id):
    # user = User.query.get_or_404(id)
    user = User.query.get(id)
    if user:
        user_response = generate_users_response(user=user)
        return jsonify(user_response), 200
    else:  # user is None:
        return jsonify({"error": f"user with the id {id} not exist"}), 404
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
    print(data)
    new_user = User(name=escape(data['name']), email=data['email'], password=data['password'], age=data['age'])
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({
            'message': 'user created',
            'user': {
                'id': new_user.id,
                'name': new_user.name,
            }

        }), 201
    except IntegrityError as ex:
        db.session.rollback()
        return jsonify({'error': f'user with email: {data['email']} already exists'}), 400
