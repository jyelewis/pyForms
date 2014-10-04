import random

import pyForms
import tornado

import html


import customControls
pyForms.registerControl("highlight", customControls.Highlight)
pyForms.registerControl("winner", customControls.Winner)


import webpages.index
myFirstWebpage = pyForms.Page(webpages.index.controller)

import webpages.chat
chatPage = pyForms.Page(webpages.chat.controller)

import webpages.loopTesting
loopTestingPage = pyForms.Page(webpages.loopTesting.Controller)


#START WEB SERVERY STUFF
import tornado.ioloop
import tornado.web


application = tornado.web.Application([
    (r"/", pyForms.tornadoHandler(myFirstWebpage)),
    (r"/chat", pyForms.tornadoHandler(chatPage)),
    (r"/loopTesting", pyForms.tornadoHandler(loopTestingPage)),
])

application.listen(8888)
tornado.ioloop.IOLoop.instance().start()


