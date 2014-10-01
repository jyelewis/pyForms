import random

import pyForms
import tornado

import html


import customControls
pyForms.registerControl("highlight", customControls.Highlight)
pyForms.registerControl("winner", customControls.Winner)


code = """
	<winner server odds="3" failtext="Not today, sorry" id="mainWinner">
		<highlight server>You are a winner!!</highlight>
	</winner>
	<h1 id="h1Test" visible="true" test="blah">This is a test</h1>
	<a href="#" id="randLink">This is a link to something</a>
	<form method='post'>
		<input type="hidden" name="pyForms__postbackInstanceID" id="hdnPostBack" />
		<input type="submit" value="test" name="btn" />
		<textbox id="tbxLink" server /><br>
		<textbox server id="mahTextarea" /><br>
		<textbox server /><br>
		<TextBox server /><br>
		<button server id="btnTextarea">toggle textarea</button>
	</form>
"""

class myPageController(pyForms.PageController):
	def onInit(self):
		self.pageStr = str(random.randint(1, 100))

	def onLoad(self):
		self.page.controls["randLink"].innerHTML = "This is a <highlight id='hideMe' server>link</highlight> to " + html.escape(self.page.controls['tbxLink'].text)

		print(self.page.controls)
		test = self.page.controls['hideMe']
		self.page.controls['hdnPostBack'].attributes["value"] = self.page.id

	def btnTextarea_click(self):
		btnTextarea = self.page.controls['btnTextarea']
		textarea = self.page.controls['mahTextarea']
		if textarea.type == "singleline":
			textarea.type = "textarea"
		else:
			textarea.type = "singleline"

myFirstWebpage = pyForms.Page(code, myPageController)



#START WEB SERVERY STUFF
import tornado.ioloop
import tornado.web


application = tornado.web.Application([
    (r"/", pyForms.tornadoHandler(myFirstWebpage)),
])

application.listen(8888)
tornado.ioloop.IOLoop.instance().start()


