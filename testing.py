import pyForms
import tornado

import customControls
pyForms.registerControl("highlight", customControls.Highlight)
pyForms.registerControl("winner", customControls.Winner)



code = """
	<winner server odds="2000" failtext="Not today, sorry" id="mainWinner">
		<highlight server>You are a winner!!</highlight>
	</winner>
"""

class myPageController(pyForms.PageController):
	def onInit(self):
		print("page inited!")

	def onLoad(self):
		print("page loaded!")
		self.page.controls["mainWinner"].odds = 1

	def onPrerender(self):
		print("page prerendered?")

myFirstWebpage = pyForms.Page(code, myPageController)



#START WEB SERVERY STUFF
import tornado.ioloop
import tornado.web


application = tornado.web.Application([
    (r"/", pyForms.tornadoHandler(myFirstWebpage)),
])

application.listen(8888)
tornado.ioloop.IOLoop.instance().start()


