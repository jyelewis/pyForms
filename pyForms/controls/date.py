import datetime

import pyForms.customControl

class Control(pyForms.customControl.Base):
	def render(self):
		today = datetime.date.today()
		return today.strftime(self.innerHTML)
