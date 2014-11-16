import pyForms
import random
import cgi

class Controller(pyForms.PageController):
	def setHTMLFile(self):
		self.HTMLFile = "webpages/includeTest.html"

	def btnRand_click(self, ctrls):
		ctrls.divRand.innerHTML = str(random.randint(0,100000))

