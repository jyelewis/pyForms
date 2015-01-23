import random 
import pyForms

class Controller(pyForms.PageController):
	def setHTMLFile(self):
		self.HTMLFile = "webpages/anonValidators.html"

	def onInit(self, ctrls):
		formCtrls = pyForms.parser.parse("""<textbox server placeholder="Integer" /><validator:range server>Please enter a valid integer</validator:range>""", self.page)
		formCtrls[1].control = formCtrls[0]
		ctrls.validationGroupCtrl.children.append(formCtrls[0])
		ctrls.validationGroupCtrl.children.append(formCtrls[1])


	def onLoad(self, ctrls):
		pass
