from flask import Blueprint, render_template, request, redirect, url_for, session
from ..models.server import Server

server_bp = Blueprint('server', __name__, url_prefix='/servers')


@server_bp.route('/escolher', methods=['GET', 'POST'])
def choose_server():
    if 'user_id' not in session:
        return redirect(url_for('auth.login_form'))
    servers = Server.query.all()
    if request.method == 'POST':
        server_id = request.form.get('server_id')
        server = Server.query.filter_by(id=server_id).first_or_404()
        session['server_id'] = server.id
        session['server_name'] = server.name
        return redirect(url_for('upload.index'))
    return render_template('server_select.html', servers=servers)
