from flask import Flask, jsonify, request

app = Flask(__name__)

# A simple route that returns a message
@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the Flask App!'}), 200

# A route that adds two numbers
@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    if a is None or b is None:
        return jsonify({'error': 'Missing parameters'}), 400
    return jsonify({'result': a + b})

# A route that fetches data from a mock database (for testing)
@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    users = {
        1: {'name': 'Alice', 'age': 30},
        2: {'name': 'Bob', 'age': 25},
    }
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
