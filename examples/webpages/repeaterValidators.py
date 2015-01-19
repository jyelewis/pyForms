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

	def btnNew2_click(self, ctrls):
		ctrls.lpItems2.append("")
		ctrls.lpItems2.reconfigure()

	def lpItems_configureLoop(self, ctrls, loopCtrls, item, index):
		def clickHandler():
			ctrls.lpItems.remove(index)
			ctrls.lpItems.reconfigure()

		loopCtrls.btnDelete.clickHandler = clickHandler
		loopCtrls.valTbx.control = loopCtrls.tbx

	def lpItems2_configureLoop(self, ctrls, loopCtrls, item, index):
		def clickHandler():
			ctrls.lpItems2.remove(index)
			ctrls.lpItems2.reconfigure()

		loopCtrls.btnDelete.clickHandler = clickHandler
		loopCtrls.valTbx.control = loopCtrls.tbx