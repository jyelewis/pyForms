import pyForms

class Controller(pyForms.PageController):
	def setHTMLFile(self):
		self.HTMLFile = "webpages/loopTesting.html"

	def onInit(self, ctrls):
		ctrls.lpItems.dataSource = []

	def onPrerender(self, ctrls):
		ctrls.pnlCount.innerHTML = str(len(ctrls.lpItems.dataSource))

	def btnNew_click(self, ctrls):
		ctrls.lpItems.append("")
		ctrls.lpItems.reconfigure()

	def lpItems_configureLoop(self, ctrls, loopCtrls, item, index):
		def clickHandler():
			ctrls.lpItems.remove(index)
			ctrls.lpItems.reconfigure()

		loopCtrls.btnDelete.clickHandler = clickHandler