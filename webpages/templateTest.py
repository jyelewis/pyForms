import random
import pyForms

class Controller(pyForms.PageController):
	def setHTMLFile(self):
		self.HTMLFile = "webpages/templateTest.html"

		import webpages.template
		self.template = webpages.template.Controller

	def onInit(self, ctrls):
		ctrls.pNumber.innerHTML = "init!:" + str(random.randint(100,999))

	def btnNumber_click(self, ctrls):
		ctrls.pNumber.innerHTML = str(random.randint(100,999))

	