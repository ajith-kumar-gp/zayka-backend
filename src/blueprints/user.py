from flask import Blueprint, request
from src.handlers.user.login import UserHandler

user_blueprint = Blueprint("user", __name__)
handler = UserHandler()

@user_blueprint.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not all([username, email, password]):
        return {"status": False, "message": "All fields are required"}, 400

    return handler.register_user(username, email, password)



# login endpoint---------
@user_blueprint.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not all([email, password]):
        return {"status": False, "message": "Email and password are required"}, 400

    return handler.login_user(email, password)

