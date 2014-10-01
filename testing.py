import random

import pyForms
import tornado

import html


import customControls
pyForms.registerControl("highlight", customControls.Highlight)
pyForms.registerControl("winner", customControls.Winner)


import webpages.index
myFirstWebpage = pyForms.Page(webpages.index.controller)



#START WEB SERVERY STUFF
import tornado.ioloop
import tornado.web


application = tornado.web.Application([
    (r"/", pyForms.tornadoHandler(myFirstWebpage)),
])

application.listen(8888)
tornado.ioloop.IOLoop.instance().start()


