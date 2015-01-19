import pyForms

secretPassword = "password"

class Controller(pyForms.PageController):
	def setHTMLFile(self):
		self.HTMLFile = "webpages/redirect.html"

	def btnRedirect_click(self, ctrls):
		if ctrls.tbxPassword.text == secretPassword:
			#redirect here
			self.page.response.redirect('http://google.com.au')
		else:
			ctrls.pnlErrorMessage.visible = True
