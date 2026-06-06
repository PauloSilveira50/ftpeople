from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect, text

db = SQLAlchemy()

_SEED_SERVERS = [
    {"name": "Servidor Dev",      "host": "ftp.dev.local",      "port": 21, "username": "dev_user",     "password": "dev_pass"},
    {"name": "Servidor Staging",  "host": "ftp.staging.local",  "port": 21, "username": "staging_user", "password": "staging_pass"},
    {"name": "Servidor Produção", "host": "ftp.producao.local", "port": 21, "username": "prod_user",    "password": "prod_pass"},
]

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SECRET_KEY'] = 'dev'

    db.init_app(app)

    from .routes.upload_routes import upload_bp
    from .routes.update_routes import update_bp
    from .routes.delete_routes import delete_bp
    from .routes.auth_routes import auth_bp
    from .routes.server_routes import server_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(upload_bp)
    app.register_blueprint(update_bp)
    app.register_blueprint(delete_bp)
    app.register_blueprint(server_bp)

    @app.route("/")
    def home():
        return redirect(url_for("auth.login_form"))

    with app.app_context():
        from .models.project import Project
        from .models.user import User
        from .models.server import Server
        db.create_all()

        existing_columns = [col['name'] for col in inspect(db.engine).get_columns('project')]
        if 'server_id' not in existing_columns:
            db.session.execute(text('ALTER TABLE project ADD COLUMN server_id INTEGER REFERENCES server(id)'))
            db.session.commit()

        if Server.query.count() == 0:
            for s in _SEED_SERVERS:
                db.session.add(Server(**s))
            db.session.commit()

    return app
