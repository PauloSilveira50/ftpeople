from flask import Blueprint, request, render_template, redirect, url_for, flash, session
from datetime import datetime
from .. import db
from ..models.project import Project
import os
import shutil

delete_bp = Blueprint('delete', __name__, url_prefix="/delete")


def _guard():
    if 'user_id' not in session:
        return redirect(url_for('auth.login_form'))
    if 'server_id' not in session:
        return redirect(url_for('server.choose_server'))
    return None


@delete_bp.route("/", methods=["GET", "POST"])
def delete_file():
    guard = _guard()
    if guard:
        return guard
    server_id = session['server_id']

    if request.method == "POST":
        project_name = request.form.get("project_name")

        if not project_name:
            flash("Informe o nome do projeto!", "error")
            return redirect(url_for("delete.delete_file"))

        project = Project.query.filter_by(name=project_name, server_id=server_id).first()

        if not project:
            flash("Projeto não encontrado!", "error")
            return redirect(url_for("delete.delete_file"))

        filepath = os.path.join("uploads", str(server_id), project.filename)
        if os.path.exists(filepath):
            trash_folder = os.path.join("uploads", str(server_id), "excluidos")
            os.makedirs(trash_folder, exist_ok=True)
            shutil.move(filepath, os.path.join(trash_folder, project.filename))

        project.delete_date = datetime.now()
        db.session.commit()

        flash("Arquivo deletado com sucesso!", "success")
        return redirect(url_for("delete.delete_file"))

    return render_template("delete.html")
