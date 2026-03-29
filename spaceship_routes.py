from flask import Blueprint, jsonify, request, abort
from app.models.spaceship import Spaceship
from app.storage import spaceships

spaceship_bp = Blueprint('spaceships', __name__)


@spaceship_bp.route('/spaceships', methods=['GET'])
def get_spaceships():
    return jsonify([s.to_dict() for s in spaceships])


@spaceship_bp.route('/spaceships', methods=['POST'])
def create_spaceship():
    data = request.get_json()

    if not data or 'name' not in data or 'type' not in data:
        abort(400)

    spaceship = Spaceship(len(spaceships) + 1, data['name'], data['type'])
    spaceships.append(spaceship)

    return jsonify(spaceship.to_dict()), 201


@spaceship_bp.route('/spaceships/<int:ship_id>', methods=['PUT'])
def update_spaceship(ship_id):
    data = request.get_json()

    spaceship = next(
        (s for s in spaceships if s.spaceship_id == ship_id), None)

    if spaceship is None:
        abort(404)

    if not data or 'status' not in data:
        abort(400)

    spaceship.update_status(data['status'])
    return jsonify(spaceship.to_dict())


@spaceship_bp.route('/spaceships/<int:ship_id>', methods=['DELETE'])
def delete_spaceship(ship_id):
    global spaceships

    spaceship = next(
        (s for s in spaceships if s.spaceship_id == ship_id), None)

    if spaceship is None:
        abort(404)

    spaceships.remove(spaceship)
    return jsonify({"message": "Deleted"})
