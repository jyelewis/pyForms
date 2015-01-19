import pyForms

class Controller(pyForms.PageController):
	def setHTMLFile(self):
		self.HTMLFile = "webpages/session.html"

	def onInit(self, ctrls):
		self.currentEditingIndex = None

		if not 'notes' in self.request.session:
			self.request.session['notes'] = []

	def onPrerender(self, ctrls):
		ctrls.drpText.dataSource = [(x['name'], index) for index, x in enumerate(self.request.session['notes'])]
		if self.currentEditingIndex is not None:
			ctrls.drpText.selectedValue = self.currentEditingIndex
		ctrls.btnEdit.visible = len(ctrls.drpText.dataSource) > 0

	def btnEdit_click(self, ctrls):
		selectedItem = self.request.session['notes'][ctrls.drpText.selectedValue]
		self.editItem(selectedItem['name'], selectedItem['content'], ctrls.drpText.selectedValue)

	def btnNew_click(self, ctrls):
		self.editItem()

	def btnSave_click(self, ctrls):
		newObj = {'name': ctrls.tbxName.text, 'content': ctrls.tbxContent.text}
		if self.currentEditingIndex is None:
			self.request.session['notes'].append(newObj)
			self.currentEditingIndex = len(self.request.session['notes']) - 1
		else:
			self.request.session['notes'][self.currentEditingIndex] = newObj

		ctrls.pnlEdit.visible = False
		ctrls.pnlChoose.visible = True

	def btnCancel_click(self, ctrls):
		ctrls.pnlEdit.visible = False
		ctrls.pnlChoose.visible = True
		

	def editItem(self, name = "", content = "", index = None):
		tbxName = self.page.controls['tbxName']
		tbxContent = self.page.controls['tbxContent']

		tbxName.text = name
		tbxContent.text = content

		self.currentEditingIndex = index
		self.page.controls['pnlEdit'].visible = True
		self.page.controls['pnlChoose'].visible = False











