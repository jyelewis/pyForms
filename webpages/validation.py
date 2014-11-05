import random 
import pyForms

class Controller(pyForms.PageController):
	def setHTMLFile(self):
		self.HTMLFile = "webpages/validation.html"

	def onInit(self, ctrls):
		pass
		#ctrls.tbxTest1.validators.append(pyForms.validator)

	def onLoad(self, ctrls):
		if self.page.request.isValid:
			ctrls.tbxTest2.text = random.randint(100000,999999)