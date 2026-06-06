from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from datetime import datetime
from .. import db
from ..models.project import Project
import os

update_bp = Blueprint('update', __name__, url_prefix="/update")


def _guard():
    if 'user_id' not in session:
        return redirect(url_for('auth.login_form'))
    if 'server_id' not in session:
        return redirect(url_for('server.choose_server'))
    return None


@update_bp.route("/", methods=["GET", "POST"])
def update_file():
    guard = _guard()
    if guard:
        return guard
    server_id = session['server_id']

    if request.method == "POST":
        project_name = request.form.get("project_name")
        file = request.files.get("file")

        if not project_name or not file or file.filename == "":
            flash("Preencha todos os campos e selecione um arquivo!", "error")
            return redirect(url_for("update.update_file"))

        update_folder = os.path.join("updates", str(server_id))
        os.makedirs(update_folder, exist_ok=True)
        file.save(os.path.join(update_folder, file.filename))

        project = Project.query.filter_by(name=project_name, server_id=server_id).first()
        if project:
            project.filename = file.filename
            project.update_date = datetime.now()
        else:
            project = Project(
                name=project_name,
                filename=file.filename,
                update_date=datetime.now(),
                server_id=server_id,
            )
            db.session.add(project)

        db.session.commit()

        flash("Arquivo atualizado com sucesso!", "success")
        return redirect(url_for("update.update_file"))

    return render_template("update.html")
