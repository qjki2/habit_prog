from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date

class User(db.Model):
    __tablename__ = 'users'

    id_U = db.Column(db.Integer, primary_key=True) #PK
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    #relationships
    habits_seguiti = db.relationship('SegueHabit', back_populates='user')

    def set_password(self, raw_password):
        self.password_hash = generate_password_hash(raw_password)

    def check_password(self, raw_password):
        return check_password_hash(self.password_hash, raw_password)

class Habit(db.Model):
    __tablename__ = 'habits'

    id_H = db.Column(db.Integer, primary_key=True) #PK
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(255))
    streak = db.Column(db.Integer, default=0)

    utenti_seguiti = db.relationship('SegueHabit', back_populates='habit')

class SegueHabit(db.Model): #tabella ponte tra user e habit
    __tablename__ = 'segue_habit'

    id_U= db.Column(db.Integer, db.ForeignKey('users.id_U'), primary_key=True)
    id_H = db.Column(db.Integer, db.ForeignKey('habits.id_H'), primary_key=True)

    data_inizio = db.Column(db.DateTime, nullable=False)

    #relationships
    user = db.relationship('User', back_populates='habits_seguiti')
    habit = db.relationship('Habit', back_populates='utenti_seguiti')

class HabitLog(db.Model):
    __tablename__ = 'habit_logs'

    id_L = db.Column(db.Integer, primary_key=True)
    id_U = db.Column(db.Integer, db.ForeignKey('users.id_U'), nullable=False)
    id_H = db.Column(db.Integer, db.ForeignKey('habits.id_H'), nullable=False)
    data = db.Column(db.Date, default=date.today, nullable=False)
    completato = db.Column(db.Boolean, default=True, nullable=False)

    # Relazioni
    user = db.relationship('User', back_populates='logs')
    habit = db.relationship('Habit', back_populates='logs')

    # Garantisce che un utente possa fare solo un check-in al giorno per la stessa abitudine
    __table_args__ = (
        db.UniqueConstraint('id_U', 'id_H', 'data', name='_user_habit_daily_uc'),
    )