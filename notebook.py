from flask import Flask, request
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


@app.route('/notes/new', methods=('GET', 'POST'))
def create_note():
    notesDB = get_notesdb()

    response = {}

    print(request.values)
    title = request.values.get('title', "some name")
    text = request.values.get('text', "some text")
    note = notesDB.createAndAddNewNote(title, text)

    response["status"] = 'OK'
    response["note_id"] = note.getID()


    return json.dumps(response)
