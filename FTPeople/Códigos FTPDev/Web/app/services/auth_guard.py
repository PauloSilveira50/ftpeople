from flask import session, jsonify

def require_login(func):
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            return jsonify({"error": "Não autorizado"}), 401
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper
