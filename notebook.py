from flask import Flask
import json

from utils import NotesDB


app = Flask(__name__)


def get_notesdb():
    notesDB = NotesDB()
    notesDB.start()
    return notesDB


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/notes')
def get_last_notes_id():
    notesDB = get_notesdb()

    response = {}
    response["last_id"] = notesDB.getLastID()

    return json.dumps(response)


@app.route('/notes/<int:note_id>')
def get_note(note_id):
    notesDB = get_notesdb()
    note = notesDB.getNoteById(note_id)

    response = {}

    if note is not None:
        response["note"] = note.dumpToDict()
    else:
        response["note"] = None

    return json.dumps(response)
