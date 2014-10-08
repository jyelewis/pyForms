import pyForms

users = []
messages = []

class controller(pyForms.PageController):
	def setHTMLFile(self):
		self.HTMLFile = "webpages/chat.html"

	def onInit(self, ctrls):
		self.username = None
		if 'chatUsername' in self.request.cookies:
			self.login(self.request.cookies['chatUsername'])

		#bind the loop
		ctrls.lpMessages.dataSource = messages

	def onPrerender(self, ctrls):
		#get latest message
		ctrls.pnlLogin.visible = not self.isLoggedIn
		ctrls.pnlChat.visible = self.isLoggedIn

		if self.isLoggedIn and len(messages) > 0:
			ctrls.lpMessages.update()

	@property
	def isLoggedIn(self):
		return (self.username is not None)

	def btnLogin_click(self, ctrls):
		if ctrls.tbxName.text in users:
			ctrls.pnlLoginError.visible = True
			return

		ctrls.pnlLoginError.visible = False

		self.login(ctrls.tbxName.text)

		
	def btnSendMessage_click(self, ctrls):
		messages.append((ctrls.tbxMessage.text, self.username))
		ctrls.tbxMessage.text = "" #empty the textbox

	def lpMessages_configureLoop(self, ctrls, loopCtrls, data, index):
		loopCtrls.messageText.innerHTML = data[0]
		loopCtrls.saidBy.innerHTML = data[1]

	def btnLogout_click(self, ctrls):
		self.logout()

	def login(self, username):
		self.username = username
		self.request.setCookie('chatUsername', self.username, {
				 'expires': None #expire at end of session
				 ,'domain': None
				 ,'path': "/"
			}) #NOTE these are all defaults, just example code
		self.page.controls['pnlName'].innerHTML = self.username
		users.append(self.username)


	def logout(self):
		del users[users.index(self.username)]
		self.username = None
		self.request.clearCookie('chatUsername')
		self.page.controls['pnlName'].innerHTML = 'Not logged in'












