import random

import pyForms.CustomControl

class Control(pyForms.CustomControl.Base):
	def __init__(self, obj):
		super().__init__(obj)

		#render config
		self.tagname = "input"
		self.isSelfClosing = True
		self.attributes['type'] = 'submit'

		self.name = str(random.randint(100,999))
		if self.id is not None:
			self.name = self.id + "_" + self.name

		self.attributes['name'] = self.name
		self.clickHandler = self.getEventHandler("click")

	def fireEvents(self):
		if self.name in self.pageInstance.request.post and self.clickHandler:
			self.clickHandler()

	def render(self):
		self.attributes['value'] = self.innerHTML
		return super().render()