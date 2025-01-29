# routes.py
from flask import Blueprint, request, jsonify
from bson import ObjectId
from app import mongo
from app.models import User

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/users', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    return jsonify([User.serialize(user) for user in users]), 200

@user_routes.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = mongo.db.users.find_one({"_id": ObjectId(id)})
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(User.serialize(user)), 200

@user_routes.route('/users', methods=['POST'])
def create_user():
    data = request.json
    if not data.get('name') or not data.get('email') or not data.get('password'):
        return jsonify({"error": "Missing required fields"}), 400

    hashed_password = User.hash_password(data['password'])
    new_user = {
        "name": data['name'],
        "email": data['email'],
        "password": hashed_password
    }
    result = mongo.db.users.insert_one(new_user)
    return jsonify({"id": str(result.inserted_id)}), 201

@user_routes.route('/users/<id>', methods=['PUT'])
def update_user(id):
    data = request.json
    user = mongo.db.users.find_one({"_id": ObjectId(id)})
    if not user:
        return jsonify({"error": "User not found"}), 404

    update_data = {}
    if data.get('name'):
        update_data['name'] = data['name']
    if data.get('email'):
        update_data['email'] = data['email']
    if data.get('password'):
        update_data['password'] = User.hash_password(data['password'])

    mongo.db.users.update_one({"_id": ObjectId(id)}, {"$set": update_data})
    return jsonify({"message": "User updated"}), 200

@user_routes.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    result = mongo.db.users.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"message": "User deleted"}), 200
