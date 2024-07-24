from flask import Blueprint, request, jsonify
from models.note import Note, get_all_notes, get_note_by_id, add_note, update_note, delete_note

note_blueprint = Blueprint('note', __name__)

@note_blueprint.route('/notes', methods=['GET'])
def get_notes():
    notes = get_all_notes()
    return jsonify(notes), 200

@note_blueprint.route('/notes/<int:note_id>', methods=['GET'])
def get_note(note_id):
    note = get_note_by_id(note_id)
    if note:
        return jsonify(note), 200
    return jsonify({'message': 'Note not found'}), 404

@note_blueprint.route('/notes', methods=['POST'])
def create_note():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    new_note = add_note(title, content)
    return jsonify(new_note), 201

@note_blueprint.route('/notes/<int:note_id>', methods=['PUT'])
def update_existing_note(note_id):
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    updated_note = update_note(note_id, title, content)
    if updated_note:
        return jsonify(updated_note), 200
    return jsonify({'message': 'Note not found'}), 404

@note_blueprint.route('/notes/<int:note_id>', methods=['DELETE'])
def delete_existing_note(note_id):
    if delete_note(note_id):
        return jsonify({'message': 'Note deleted successfully'}), 200
    return jsonify({'message': 'Note not found'}), 404