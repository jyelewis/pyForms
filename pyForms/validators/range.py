import pyForms.ControlBase
from pyForms.validators import Base

import pyForms.controls.Textbox

class Control(Base.Class):
	def initValidator(self):
		if not type(self.control) is pyForms.controls.Textbox.Control:
			raise Exception("Non textbox control given to range validator")
			return

		self.serverValidator = self.ctrl_textbox
		self.clientCode = "return !isNaN(document.getElementById('"+ self.control.attributes['id'] +"').value);"

		
	def onRequest(self):
		#show error thingy if there is an error thingy
		if self.pageInstance.request.isPostBack:
			self.isValid = self.serverValidator()
			self.pageInstance.isValid = self.isValid


	def ctrl_textbox(self):
		try:
			float(self.control.text)
			return True
		except ValueError:
			return False






