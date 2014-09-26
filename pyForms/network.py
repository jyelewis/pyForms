#These classes must be subclassed to generate objects for specific server frameworks

class Request():
	def __init__(self):
		self.url = None
		self.get = {}
		self.post = {}


class Response():
	def __init__(self):
		pass

	def write(self):
		raise NotImplimentedError

	def end(self):
		pass

	def redirect(self):
		raise NotImplimentedError



