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

code = """
	code:
	<winner server odds="2">
		<highlight server>You are a winner!!</highlight>
		<winner server odds="3">Double winner!</winner>
	</winner>
"""
myFirstWebpage = pyForms.Page(code)
print(myFirstWebpage.render())
