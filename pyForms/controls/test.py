import pyForms.CustomControl

class Control(pyForms.CustomControl.Base):
	def render(self):
		return '<strong>'+ self.innerHTML +'</strong>'