import pyForms.PageController

class Controller(pyForms.PageController):
	def setHTMLFile(self):
		self.HTMLFile = "webpages/nestedLoops.html"

	def onInit(self, ctrls):
		ctrls.lpRows.dataSource = []

	def btnNewRow_click(self, ctrls):
		ctrls.lpRows.append([""])

	def lpRows_configureLoop(self, ctrls, loopCtrls, item, index):
		loopCtrls.lpColumns.dataSource = item

		def newColHandler():
			loopCtrls.lpColumns.append("")

		loopCtrls.btnNewCol.clickHandler = newColHandler