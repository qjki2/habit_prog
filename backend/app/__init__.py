import os
from flask import Flask
from flask_cors import CORS
from app.extensions import db, ma
from app.models.habit import User

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Configura il collegamento a PostgreSQL
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inizializza le estensioni
    db.init_app(app)
    ma.init_app(app)

    # CREAZIONE EFFETTIVA DELLE TABELLE NEL DATABASE
    with app.app_context():
        # Legge i modelli Python e invia i comandi SQL 'CREATE TABLE IF NOT EXISTS' a Postgres
        db.create_all()
        if not User.query.first():
            # Se non ci sono utenti, crea un utente di default
            default_user = User(username="default_user", email = "admin@g.com")
            default_user.set_password("admin123")
            db.session.add(default_user)
            db.session.commit()

    return app