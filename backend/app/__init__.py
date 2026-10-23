import os
from flask import Flask
from flask_cors import CORS
from app.extensions import db, ma

# IMPORTANTE: Importa i modelli affinché SQLAlchemy riconosca le classi
from app.models.habit import User, Habit, SegueHabit, HabitLog

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

    return app