from flask import Blueprint, request
from controllers.connect_controller import (
    create_user,
    list_users,
    get_user_by_id
)

connect_bp = Blueprint("connect", __name__)


@connect_bp.post("/users")
def register_user():
    data = request.get_json(silent=True)
    return create_user(data)


@connect_bp.get("/users")
def get_users():
    return list_users()


@connect_bp.get("/users/<int:user_id>")
def get_user(user_id):
    return get_user_by_id(user_id)