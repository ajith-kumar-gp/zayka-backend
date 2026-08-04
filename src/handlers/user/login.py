import datetime

import bcrypt
import jwt
from flask import current_app

from src.data import store


class UserHandler:
    def _create_token(self, user):
        return jwt.encode(
            {
                "user_id": user["user_id"],
                "email": user["email"],
                "role": user.get("user_role", "User"),
                "cartdata": user.get("cartdata", {}),
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2),
            },
            current_app.config["SECRET_KEY"],
            algorithm="HS256",
        )

    def register_user(self, username, email, password):
        username = username.strip()
        email = email.strip().lower()

        def add_user(data):
            users = data.setdefault("users", [])
            existing_user = next(
                (user for user in users if user.get("email", "").lower() == email),
                None,
            )
            if existing_user:
                return {"status": False, "message": "Email already registered"}, 200

            next_id = max((int(user.get("user_id", 0)) for user in users), default=0) + 1
            hashed_pw = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
            user = {
                "user_id": next_id,
                "username": username,
                "email": email,
                "password": hashed_pw.decode("utf-8"),
                "cartdata": {},
                "user_role": "User",
            }
            users.append(user)
            return {
                "status": True,
                "message": "User registered successfully",
                "token": self._create_token(user),
            }, 201

        return store.update(add_user)

    def login_user(self, email, password):
        email = email.strip().lower()
        data = store.read()
        user = next(
            (item for item in data.get("users", []) if item.get("email", "").lower() == email),
            None,
        )

        if not user:
            return {"status": False, "message": "User doesnt exist"}, 401

        if not bcrypt.checkpw(password.encode("utf-8"), user["password"].encode("utf-8")):
            return {"status": False, "message": "Invalid email or password"}, 401

        return {
            "status": True,
            "message": "Login successful",
            "token": self._create_token(user),
        }, 200
