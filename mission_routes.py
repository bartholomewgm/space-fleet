from flask import Blueprint, jsonify, request, abort
from app.models.mission import Mission
from app.storage import missions, spaceships

mission_bp = Blueprint('missions', __name__)


@mission_bp.route('/missions', methods=['GET'])
def get_missions():
    return jsonify([m.to_dict() for m in missions])


@mission_bp.route('/missions', methods=['POST'])
def create_mission():
    data = request.get_json()

    if not data or 'name' not in data or 'goal' not in data:
        abort(400)

    mission = Mission(len(missions) + 1, data['name'], data['goal'])
    missions.append(mission)

    return jsonify(mission.to_dict()), 201


@mission_bp.route('/missions/<int:mission_id>/add_ship/<int:ship_id>', methods=['POST'])
def add_ship(mission_id, ship_id):
    mission = next((m for m in missions if m.mission_id == mission_id), None)
    spaceship = next(
        (s for s in spaceships if s.spaceship_id == ship_id), None)

    if mission is None or spaceship is None:
        abort(404)

    mission.add_spaceship(spaceship)
    return jsonify(mission.to_dict())
