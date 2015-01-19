import pyForms
import cgi

class Controller(pyForms.PageController):
	def setHTMLFile(self):
		self.HTMLFile = "webpages/include.html"

	def tbxName_change(self, ctrls, oldVal):
		ctrls.divName.innerHTML = ctrls.tbxName.text

