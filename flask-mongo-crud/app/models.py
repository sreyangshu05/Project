# models.py
from werkzeug.security import generate_password_hash, check_password_hash

class User:
    @staticmethod
    def serialize(user):
        return {
            "id": str(user["_id"]),
            "name": user["name"],
            "email": user["email"],
        }

    @staticmethod
    def hash_password(password):
        return generate_password_hash(password)

    @staticmethod
    def verify_password(hash, password):
        return check_password_hash(hash, password)
