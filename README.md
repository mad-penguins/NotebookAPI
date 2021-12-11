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
