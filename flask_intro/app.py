# pip install Flask
# create a directory flask_intro
# create a file app.py
# pip install SQLAlchemy
# pip install -U Flask-SQLAlchemy
# pip install Flask-JWT-Extended
# pip install Flask-Migrate
# pip install Flask-Limiter

# ATTACKS:
# sql injection
# code / script injection

# implement login
# protect specific route to require jwt
# try to hack a route (enter with a jwt to created using jwt.io)
# make sure all db is protected (try, except, transaction, rollback())
# create middleware will escape every value from the JSON body.
# create a midleware that will print all the data before each request

"""
create a full rest api backend for users.
you need to implement the following:
create user
get all users
get one user by id
get one user by name
update user
update all users
delete user
delete all users

bonus:
get average of all ages
count how many users
get the sum of all ages
get all the users that has a Gmail.

"""
from flask import Flask, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_migrate import Migrate
from sqlalchemy.exc import IntegrityError
from users.models import db
from users.routes import users_bp
from flask_jwt_extended import JWTManager

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'MOCK_SECRET_123456'

jwt = JWTManager(app)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://",
)

@app.route('/test', methods=['GET'])
@limiter.limit('5 per minute')
def test():
    return "hello"

# init the database - extra option
# with app.app_context():
#     db.create_all()

# init the database
db.init_app(app)


migrate = Migrate(app, db)

@app.errorhandler(IntegrityError)
def handle_integrity_error(error):
    return jsonify({'error': "Duplicate email or missing data"}), 400

# @app.errorhandler(404)
# def handle_not_found_error(error):
#     print(error)
#     return jsonify({'error': 'Not found'}), 404

app.register_blueprint(users_bp)

@app.before_request
def before_request():
    print(f'Got request. method: {request.method}, URL: {request.url}. host: {request.host}')

if __name__ == '__main__':
    app.run(debug=True)

