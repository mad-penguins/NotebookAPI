# NotebookAPI
A simple server for storing notes

# How to run a server for testing

On Windows:
``` bash
$ git clone https://github.com/mad-penguins/NotebookAPI.git
$ cd NotebookAPI
$ python -m venv env
$ env\Scripts\activate.bat
$ pip install -r requirements.txt
$ set FLASK_APP=notebook.py
$ set FLASK_ENV=development
$ flask run
```

On Linux:
``` bash
$ git clone https://github.com/mad-penguins/NotebookAPI.git
$ cd NotebookAPI
$ python3 -m venv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
$ export FLASK_APP=notebook.py
$ export FLASK_ENV=development
$ flask run
```

# API
* `GET /` - returns the string 'Hello, World!'
* `GET /notes` - returns a last used ID of note
* `GET /notes/<id>` - returns a note by ID (`/notes/1`)
* `POST /notes/new` - creates a note. Returns a note ID. Parameters: `title` - title of note, `text` - content of note.
* `PUT /notes/<id>` - updates a note by ID. Parameters: `title` and `text`.
* `DELETE /notes/<id>` - deletes a note by ID.
