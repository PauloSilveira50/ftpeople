from flask import Blueprint, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from .. import db
from ..models.user import User

auth_bp = Blueprint("auth", __name__)

# FORM LOGIN (GET)
@auth_bp.route("/login", methods=["GET"])
def login_form():
    return render_template("login.html")

# LOGIN (POST)
@auth_bp.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password_hash, password):
        return "Credenciais inválidas", 401

    session["user_id"] = user.id
    return redirect(url_for("server.choose_server"))

# FORM SIGNUP (GET)
@auth_bp.route("/signup", methods=["GET"])
def signup_form():
    return render_template("signup.html")

# SIGNUP (POST)
@auth_bp.route("/signup", methods=["POST"])
def signup():
    email = request.form.get("email")
    password = request.form.get("password")

    hashed = generate_password_hash(password)

    new_user = User(email=email, password_hash=hashed)
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for("auth.login"))

# LOGOUT
@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))
