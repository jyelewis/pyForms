import datetime

import pyForms.CustomControl

class Control(pyForms.CustomControl.Base):
	def render(self):
		today = datetime.date.today()
		return today.strftime(self.innerHTML)
