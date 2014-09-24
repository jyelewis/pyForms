import pyForms

class Control(pyForms.CustomControl):
	def render(self):
		return '<strong style="font-size:24px; color:red;">'+ self.innerHTML.upper() +'</strong>'