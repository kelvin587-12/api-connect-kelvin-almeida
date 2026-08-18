from flask import jsonify
from data.connect_data import users, generate_user_id


def create_user(data):
    if not isinstance(data, dict):
        return jsonify(
            {"error": "O corpo deve conter um objeto JSON."}
        ), 400

    name = data.get("name")
    email = data.get("email")

    if not isinstance(name, str) or not name.strip():
        return jsonify(
            {"error": "O campo name é obrigatório."}
        ), 400

    if not isinstance(email, str) or not email.strip():
        return jsonify(
            {"error": "O campo email é obrigatório."}
        ), 400

    new_user = {
        "id": generate_user_id(),
        "name": name.strip(),
        "email": email.strip()
    }

    users.append(new_user)

    return jsonify({"data": new_user}), 201


def list_users():
    return jsonify({"data": users}), 200


def get_user_by_id(user_id):
    user = next(
        (user for user in users if user["id"] == user_id),
        None
    )

    if user is None:
        return jsonify(
            {"error": "Usuário não encontrado."}
        ), 404

    return jsonify({"data": user}), 200