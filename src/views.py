from flask import Blueprint, request
from src.models import Notes
from src.schemas import NotesSchema
from src import db

read_blueprint = Blueprint("read", __name__)
create_blueprint = Blueprint("create", __name__)
update_blueprint = Blueprint("update", __name__)
delete_blueprint = Blueprint("delete", __name__)

notes_schema = NotesSchema(many=True)
note_schema = NotesSchema()


@read_blueprint.route("/get-notes")
def get_notes():
    notes = Notes.query.all()
    notes_json = notes_schema.jsonify(notes)
    return notes_json


@create_blueprint.route("/create", methods=["POST"])
def create_note():
    data = request.json
    author = data["author"]
    content = data["content"]

    new_note = Notes(author=author, content=content)
    db.session.add(new_note)
    db.session.commit()

    return {"msg": "New note's been created!"}, 201


@update_blueprint.route("/update/<int:note_id>", methods=["PUT"])
def update_note(note_id):
    note = Notes.query.get(note_id)

    if note is None:
        return {"error": "Note not found"}, 404

    data = request.json
    note.author = data["author"]
    note.content = data["content"]

    db.session.commit()
    return {"msg": "Note has been updated"}, 201


@delete_blueprint.route("/delete/<int:note_id>", methods=["DELETE"])
def delete_note(note_id):
    note = Notes.query.get(note_id)

    if note is None:
        return {"error": "Note not found"}, 404

    db.session.delete(note)
    db.session.commit()
    return {"msg": "Note has been deleted"}, 201
