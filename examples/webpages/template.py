import random
import pyForms

class Controller(pyForms.TemplateController):
	def setHTMLFile(self):
		self.HTMLFile = "webpages/template.html"

	def onInit(self, ctrls):
		ctrls.pNumber.innerHTML = "init!:" + str(random.randint(100,999))

	def btnNumber_click(self, ctrls):
		ctrls.pNumber.innerHTML = str(random.randint(100,999))

