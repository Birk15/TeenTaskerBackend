from app.config import get_collection
from flask import jsonify, request

users = get_collection("Users")

def users_get():
    data = list(users.find({}))
    if data:
        for user in data:
            user['_id'] = str(user['_id'])
        return jsonify({"data": data})
    return jsonify({"error": "Fehler beim Laden der User!"})

def user_add():
    data = request.json
    if data:
        users.insert_one(data)
        return jsonify({'message': "User hinzugefügt!"}), 201
    return jsonify({'error': 'Keine Daten gesendet!'}), 400