import pyForms

class Controller(pyForms.PageController):
	def setHTMLFile(self):
		self.HTMLFile = "webpages/dropdown.html"


	def onInit(self, ctrls):
		pass
		#ctrls.ddlStates.selectedValue = "QLD"

	def onPrerender(self, ctrls):
		ctrls.pnlOther.visible = (ctrls.ddlStates.selectedValue == "Other")


	@property
	def curLocation(self):
		ddlStates = self.page.controls['ddlStates']
		tbxOther = self.page.controls['tbxOther']

		if ddlStates.selectedValue == "Other":
			return tbxOther.text
		elif ddlStates.selectedValue == "Unselected":
			return ""
		else:
			return ddlStates.selectedText