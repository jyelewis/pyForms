import pyForms

class controller(pyForms.PageController):
	def setHTMLFile(self):
		self.htmlFile = "webpages/index.html"

	def btnGo_click(self):
		tbxName = self.page.controls["tbxName"]
		pHello = self.page.controls['pHello']
		if tbxName.text == "":
			pHello.innerHTML = "You didnt enter anything!"
		else:
			pHello.innerHTML = "Hello, " + tbxName.text