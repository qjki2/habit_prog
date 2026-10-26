from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.habit import Habit

habits_bp = Blueprint('habits', __name__)

@habits_bp.route('/habits', methods=['POST'])
def create_habit():
    data = request.get_json()
    user_id = data.get('user_id',1)
    new_habit = Habit(
        title= data.get('title'),
        description= data.get('description'),
        user_id= user_id
    )

    db.session.add(new_habit)
    db.session.commit()
    return jsonify({'message': 'Habit created successfully', 'habit': {"id": new_habit.id, "title": new_habit.title}}), 201