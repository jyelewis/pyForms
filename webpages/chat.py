import pyForms

users = []
messages = []

class controller(pyForms.PageController):
	def setHTMLFile(self):
		self.HTMLFile = "webpages/chat.html"

	def onInit(self, ctrls):
		self.username = None

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

		self.username = ctrls.tbxName.text
		users.append(self.username)
		ctrls.pnlName.innerHTML = self.username

		
	def btnSendMessage_click(self, ctrls):
		messages.append((ctrls.tbxMessage.text, self.username))
		ctrls.tbxMessage.text = "" #empty the textbox

	def lpMessages_configureLoop(self, ctrls, loopCtrls, data, index):
		loopCtrls.messageText.innerHTML = data[0]
		loopCtrls.saidBy.innerHTML = data[1]














