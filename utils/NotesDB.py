import sqlite3
import datetime

from .Note import Note, getCurrentDatetime

from json import dumps, loads


def createNoteFromResponse(response):
	note = Note(response[1], response[2])

	note.ID = response[0]

	note.created = datetime.datetime.fromisoformat(str(response[3]))
	note.updated = datetime.datetime.fromisoformat(str(response[4]))

	return note


class NotesDB:
	"""docstring for NotesDB"""
	def __init__(self, dbFile="Notes.sqlite3"):
		self.mainTableName = 'notes'

		self.dbFile = dbFile
		self.conn = None
		self.lastID = 0

	def commit(self):
		self.conn.commit()

	def connect(self):
		self.conn = sqlite3.connect(self.dbFile)

	def createTable(self):
		request = 'CREATE TABLE IF NOT EXISTS ' + self.mainTableName + '(' + \
			'id INT NOT NULL PRIMARY KEY,' + \
			'title TEXT,' + \
			'text TEXT NOT NULL,' + \
			'created TEXT NOT NULL,' + \
			'updated TEXT NOT NULL' + \
			')'

		cursor = self.conn.cursor()
		cursor.execute(request)
		self.commit()

	def start(self):
		self.connect()
		self.createTable()

	def getLastID(self):
		request = 'SELECT max(id) FROM ' + self.mainTableName

		cursor = self.conn.cursor()
		cursor.execute(request)
		lastID = cursor.fetchone()[0]

		if lastID is None:
			lastID = 0

		return lastID

	def isExistsID(self, ID):
		request = 'SELECT id FROM ' + self.mainTableName + ' WHERE id = ?'

		cursor = self.conn.cursor()
		cursor.execute(request, (ID,))
		response = cursor.fetchone()

		if response is None:
			return False
		elif response[0] == ID:
			return True

	def getNoteById(self, ID):
		request = 'SELECT * FROM ' + self.mainTableName + ' WHERE id = ?'

		cursor = self.conn.cursor()
		cursor.execute(request, (ID,))
		response = cursor.fetchone()

		print(response)

		if response is None:
			return None
		else:
			return createNoteFromResponse(response)

	def createAndAddNewNote(self, title, text):
		title = str(title)
		text = str(text)
		created = datetime.datetime.now().isoformat()

		ID = self.getLastID() + 1

		data = (ID, title, text, created, created)


		request = 'INSERT INTO ' +  self.mainTableName + \
					'(id, title, text, created, updated)' + \
					'VALUES(?, ?, ?, ?, ?)'

		cursor = self.conn.cursor()
		cursor.execute(request, data)
		self.commit()

		note = self.getNoteById(ID)
		return note

	def getNumberOfAll(self):
		request = 'SELECT count(*) FROM ' + self.mainTableName

		cursor = self.conn.cursor()
		cursor.execute(request)
		response = cursor.fetchone()

		return response[0]

	def updateTitleForNote(self, note):
		request = 'UPDATE ' + self.mainTableName + ' SET title = ?' + \
					' WHERE id = ?'

		cursor = self.conn.cursor()
		cursor.execute(request, (note.getTitle(), note.getID()))
		self.commit()

	def updateTextForNote(self, note):
		request = 'UPDATE ' + self.mainTableName + ' SET text = ?' + \
					' WHERE id = ?'

		cursor = self.conn.cursor()
		cursor.execute(request, (note.getText(), note.getID()))
		self.commit()

	def updateUpdatedForNote(self, note):
		request = 'UPDATE ' + self.mainTableName + ' SET updated = ?' + \
					' WHERE id = ?'

		cursor = self.conn.cursor()
		cursor.execute(request, (note.getUpdatedDatetimeStr(), note.getID()))
		self.commit()

	def updateNote(self, note):
		if self.isExistsID(note.getID()):
			self.updateTitleForNote(note)
			self.updateTextForNote(note)
			self.updateUpdatedForNote(note)

	def deleteNoteById(self, ID):
		if self.isExistsID(ID):
			request = 'DELETE FROM ' + self.mainTableName + ' WHERE id = ?'

			cursor = self.conn.cursor()
			cursor.execute(request, (ID,))
			self.commit()
