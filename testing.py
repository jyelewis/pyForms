import pyForms
import ctrlBold


import random
class winnerControl(pyForms.CustomControl):
	def __init__(self, obj):
		super().__init__(obj)
		if not 'odds' in self.attributes:
			raise Exception("odds property was not provided!")
		self.odds = int(self.attributes['odds'])

	def render(self):
		if random.randint(1, self.odds) == 1:
			return self.innerHTML
		return ""

pyForms.registerControl("highlight", ctrlBold.Control)
pyForms.registerControl("winner", winnerControl)
#print(pyForms.render("<highlight server>This is a test</highlight>"))
print(pyForms.render('<winner server odds="2">You are a winner!!<winner server odds="2">Double winner!</winner></winner>'))