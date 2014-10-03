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


#START WEB SERVERY STUFF
import tornado.ioloop
import tornado.web


application = tornado.web.Application([
    (r"/", pyForms.tornadoHandler(myFirstWebpage)),
    (r"/chat", pyForms.tornadoHandler(chatPage)),
])

application.listen(8888)
tornado.ioloop.IOLoop.instance().start()


