from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "Ashish"},
    {"id": 2, "name": "Mitra"}
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    users.append(data)
    return jsonify({"message": "User added successfully"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

