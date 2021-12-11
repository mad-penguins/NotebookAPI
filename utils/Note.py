import datetime


def getCurrentDatetime():
	return datetime.datetime.now()


class Note:
	"""docstring for Note"""
	def __init__(self, title, text, ID=None, created=None, updated=None):
		self.ID = ID

		self.title = str(title)
		self.text = str(text)

		if created is None:
			self.created = getCurrentDatetime()
		else:
			self.created = created

		if updated is None:
			self.updated = self.created
		else:
			self.updated = updated

	def dumpToDict(self):
		d = {}

		d['id'] = self.ID

		d['title'] = self.title
		d['text'] = self.text

		d['created'] = self.created.isoformat()
		d['updated'] = self.updated.isoformat()

		return d

	def _update_datatime(self):
		self.updated = getCurrentDatetime()

	def getID(self):
		return self.ID

	def getTitle(self):
		return self.title

	def setTitle(self, title):
		self.title = str(title)
		self._update_datatime()

	def getText(self):
		return self.text

	def setText(self, text):
		self.text = str(text)
		self._update_datatime()

	def getUpdatedDatetimeStr(self):
		return self.updated.isoformat()
