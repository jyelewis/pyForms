import random
import pyForms

class controller(pyForms.PageController):
	def setHTMLFile(self):
		self.HTMLFile = "webpages/index.html"

	def onInit(self, ctrls):
		self.showingButtons = False
		self.postbackCount = 0

	def onLoad(self, ctrls):
		if self.page.request.isPostBack:
			self.postbackCount += 1
		ctrls.title.innerHTML = "Posted back " + str(self.postbackCount) + " times"

	def onPrerender(self, ctrls):
		if self.showingButtons:
			ctrls.btnToggleColourButtons.text = "Hide colour options"
			ctrls.pnlButtons.visible = True
		else:
			ctrls.btnToggleColourButtons.text = "Show colour options"
			ctrls.pnlButtons.visible = False

	def tbxName_change(self, ctrls, oldVal):
		#set defaults
		ctrls.pHello.text = ""
		ctrls.pHello.visible = True
		ctrls.divWinner.visible = False

		if ctrls.tbxName.text == "":
			ctrls.pHello.innerHTML = "You didnt enter anything!"
		elif ctrls.tbxName.text.lower() == "jye":
			ctrls.divWinner.visible = True
			ctrls.pHello.visible = False
		else:
			ctrls.pHello.innerHTML = "Hello, " + ctrls.tbxName.text

	#colour changing stuff
	def btnRed_click(self, ctrls):
		ctrls.bodyTag.attributes['style'] = "background-color:red;"

	def btnBlue_click(self, ctrls):
		ctrls.bodyTag.attributes['style'] = "background-color:blue;"

	def btnRandomColour_click(self, ctrls):
		r = lambda: random.randint(0,255)
		ctrls.bodyTag.attributes['style'] = "background-color:"+'#%02X%02X%02X' % (r(),r(),r())+";"

	def tbxCustomColour_change(self, ctrls, oldVal):
		ctrls.bodyTag.attributes['style'] = "background-color:"+ctrls.tbxCustomColour.text+";"

	def btnToggleColourButtons_click(self, ctrls):
		self.showingButtons = not self.showingButtons



