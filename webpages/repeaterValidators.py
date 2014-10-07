import pyForms

class Controller(pyForms.PageController):
	def setHTMLFile(self):
		self.HTMLFile = "webpages/repeaterValidators.html"

	def onInit(self, ctrls):
		ctrls.lpItems.dataSource = []

	@property
	def itemCount(self):
		return len(self.page.controls['lpItems'].dataSource)

	def btnNew_click(self, ctrls):
		ctrls.lpItems.append("")
		ctrls.lpItems.reconfigure()

	def lpItems_configureLoop(self, ctrls, loopCtrls, item, index):
		def clickHandler():
			ctrls.lpItems.remove(index)
			ctrls.lpItems.reconfigure()

		loopCtrls.btnDelete.clickHandler = clickHandler
		loopCtrls.valTbx.control = loopCtrls.tbx