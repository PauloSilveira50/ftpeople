from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from datetime import datetime
from .. import db
from ..models.project import Project
import os

upload_bp = Blueprint('upload', __name__, url_prefix="/upload")


def _guard():
    if 'user_id' not in session:
        return redirect(url_for('auth.login_form'))
    if 'server_id' not in session:
        return redirect(url_for('server.choose_server'))
    return None


@upload_bp.route("/", methods=["GET"])
def index():
    guard = _guard()
    if guard:
        return guard
    server_id = session['server_id']
    projects = Project.query.filter_by(delete_date=None, server_id=server_id).all()
    return render_template("index.html", projects=projects)


@upload_bp.route("/new", methods=["GET", "POST"])
def upload_file():
    guard = _guard()
    if guard:
        return guard
    server_id = session['server_id']

    if request.method == "POST":
        project_name = request.form.get("project_name")
        file = request.files.get("file")

        if not project_name or not file or file.filename == "":
            flash("Preencha todos os campos e selecione um arquivo!", "error")
            return redirect(url_for("upload.upload_file"))

        upload_folder = os.path.join("uploads", str(server_id))
        os.makedirs(upload_folder, exist_ok=True)
        file.save(os.path.join(upload_folder, file.filename))

        db.session.add(Project(
            name=project_name,
            filename=file.filename,
            upload_date=datetime.now(),
            server_id=server_id,
        ))
        db.session.commit()

        flash("Arquivo enviado com sucesso!", "success")
        return redirect(url_for("upload.index"))

    return render_template("upload.html")
