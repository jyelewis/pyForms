import pyForms

class Highlight(pyForms.CustomControl):
	def render(self):
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

	def render(self):
		if random.randint(1, self.odds) == 1:
			return self.innerHTML
		return self.failtext