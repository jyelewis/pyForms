#These classes must be subclassed to generate objects for specific server frameworks

class Request():
	def __init__(self):
		self.url = None
		self.get = {}
		self.post = {}
		self.isValid = True

		self._isPostBack = None

	@property
	def isPostBack(self):
		if self._isPostBack is None:
			self._isPostBack = ('pyForms__postbackInstanceID' in self.post)
		return self._isPostBack


class Response():
	def __init__(self):
		pass

	def write(self):
		raise NotImplimentedError

	def end(self):
		pass

	def redirect(self):
		raise NotImplimentedError



