import pyForms

class controller(pyForms.PageController):
	def setHTMLFile(self):
		self.htmlFile = "webpages/index.html"

	def onLoad(self, ctrls):
		#set defaults
		ctrls.pHello.text = ""
		ctrls.pHello.visible = True
		ctrls.divWinner.visible = False

	def btnGo_click(self, ctrls):
		if ctrls.tbxName.text == "":
			ctrls.pHello.innerHTML = "You didnt enter anything!"
		elif ctrls.tbxName.text.lower() == "jye":
			ctrls.divWinner.visible = True
			ctrls.pHello.visible = False
		else:
			ctrls.pHello.innerHTML = "Hello, " + ctrls.tbxName.text