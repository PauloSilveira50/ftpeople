from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from ..models.server import Server
from .. import db

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


@server_bp.route('/criar', methods=['POST'])
def create_server():
    if 'user_id' not in session:
        return redirect(url_for('auth.login_form'))
    name = request.form.get('name', '').strip()
    host = request.form.get('host', '').strip()
    port = request.form.get('port', '21').strip()
    username = request.form.get('username', '').strip()
    password = request.form.get('password', '').strip()
    if name and host and username and password:
        try:
            port = int(port)
        except ValueError:
            port = 21
        server = Server(name=name, host=host, port=port, username=username, password=password)
        db.session.add(server)
        db.session.commit()
    return redirect(url_for('server.choose_server'))
