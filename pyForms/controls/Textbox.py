import random

import pyForms.CustomControl

class Control(pyForms.CustomControl.Base):
	def __init__(self, obj):
		super().__init__(obj)
		self.text = ""
		self.name = str(random.randint(100,999))
		if self.id is not None:
			self.name = self.id + "_" + self.name

		self.type = "singleline"
		if "type" in self.attributes:
			self.type = self.attributes['type']
			del self.attributes['type'] #dont keep it around

		

	def onRequest(self):
		if self.name in self.pageInstance.request.post:
			self.text = self.pageInstance.request.post[self.name]

	def render(self):
		#setup for tag
		self.attributes['name'] = self.name

		if self.type.lower() in ["singleline", "password"]:
			self.attributes['type'] = "text" if self.type.lower() == "singleline" else "password"
			self.tagname = "input"
			self.isSelfClosing = True
			self.attributes['value'] = self.text
		elif self.type.lower() == "textarea":
			self.tagname = "textarea"
			self.isSelfClosing = False
			self.innerHTML = self.text
		else:
			raise Exception("Textbox type '" + self.type + "' is not valid")
		return super().render()