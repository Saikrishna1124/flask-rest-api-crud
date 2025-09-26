from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# In-memory user storage (dictionary)
users = {}


# Home Page (HTML frontend)
@app.route('/')
def home():
    return render_template("index.html")


# API: Get all users
@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users)


# API: Get single user
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({user_id: user})


# API: Create user
@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user_id = len(users) + 1
    users[user_id] = data
    return jsonify({"message": "User created", "user": {user_id: data}}), 201


# API: Update user
@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    data = request.get_json()
    users[user_id].update(data)
    return jsonify({"message": "User updated", "user": {user_id: users[user_id]}})


# API: Delete user
@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    deleted_user = users.pop(user_id)
    return jsonify({"message": "User deleted", "user": {user_id: deleted_user}})


if __name__ == '__main__':
    app.run(debug=True)
