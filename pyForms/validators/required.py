import pyForms.ControlBase
from pyForms.validators import Base

import pyForms.controls.Textbox

class Control(Base.Class):
	def initValidator(self):
		if type(self.control) is pyForms.controls.Textbox.Control:
			self.serverValidator = self.ctrl_textbox
			self.clientCode = "return document.getElementById('"+ self.control.attributes['id'] +"').value == ''; "

		elif type(self.control) is pyForms.controls.Checkbox.Control:
			self.serverValidator = self.ctrl_checkbox
			self.clientCode = "return document.getElementById('"+ self.control.attributes['id'] +"').checked == false;"

		elif type(self.control) is pyForms.controls.Dropdown.Control:
			self.serverValidator = self.ctrl_dropdown
			self.clientCode = "return document.getElementById('"+ self.control.attributes['id'] +"').selectedIndex == 0;"

		
	def onRequest(self):
		#show error thingy if there is an error thingy
		if self.pageInstance.request.isPostBack:
			self.isValid = self.serverValidator()
			self.pageInstance.isValid = self.isValid


	def ctrl_textbox(self):
		return len(self.control.text) > 0

	def ctrl_checkbox(self):
		return self.control.checked

	def ctrl_dropdown(self):
		return self.control.selectedIndex != 0







