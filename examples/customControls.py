import pyForms

class Highlight(pyForms.CustomControl):
	def render(self):
		if not self.visible:
			return ""
		return '<strong style="font-size:24px; color:red;">'+ self.innerHTML.upper() +'</strong>'


import random
class Winner(pyForms.CustomControl):
	def __init__(self, obj):
		super().__init__(obj)
		if not 'odds' in self.attributes:
			raise Exception("odds property was not provided!")
		self.odds = int(self.attributes['odds'])

		self.failtext = ""
		if 'failtext' in self.attributes:
			self.failtext = self.attributes['failtext']

		self._isWinner = None

	@property
	def isWinner(self):
		if self._isWinner is None:
			self._isWinner = (random.randint(1, self.odds) == 1)
		return self._isWinner

	def render(self):
		if not self.visible:
			return ""

		if self.isWinner:
			return self.innerHTML
		return self.failtext