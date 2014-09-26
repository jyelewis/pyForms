import pyForms
import tornado

import customControls
pyForms.registerControl("highlight", customControls.Highlight)
pyForms.registerControl("winner", customControls.Winner)



code = """
	<h1>Welcome to my humble website</h1>
	<winner server odds="2" failtext="Not today, sorry">
		<highlight server>You are a winner!!</highlight>
		<winner server odds="5">Double winner!</winner>
		<script type="text/javascript">
			/*alert('you are a winner!');
			alert('<winner server odds="2">Double winner!</winner>');*/
		</script>
		
	</winner>
"""

class myPageController(pyForms.PageController):
	def onInit(self):
		print("page inited!")

	def onLoad(self):
		print("page loaded!")

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


