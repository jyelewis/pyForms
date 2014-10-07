import sys

import pyForms
import tornado


import customControls
pyForms.registerControl("highlight", customControls.Highlight)
pyForms.registerControl("winner", customControls.Winner)


import webpages.index
myFirstWebpage = pyForms.Page(webpages.index.controller)

import webpages.chat
chatPage = pyForms.Page(webpages.chat.controller)

import webpages.loopTesting
loopTestingPage = pyForms.Page(webpages.loopTesting.Controller)

import webpages.validation
validationPage = pyForms.Page(webpages.validation.Controller)

import webpages.dropdown
dropdownPage = pyForms.Page(webpages.dropdown.Controller)

import webpages.repeaterValidators
repeaterValidatorsPage = pyForms.Page(webpages.repeaterValidators.Controller)

import webpages.file
filePage = pyForms.Page(webpages.file.Controller)


#START WEB SERVERY STUFF
import tornado.ioloop
import tornado.web


application = tornado.web.Application([
    (r"/", pyForms.tornadoHandler(myFirstWebpage)),
    (r"/chat", pyForms.tornadoHandler(chatPage)),
    (r"/loopTesting", pyForms.tornadoHandler(loopTestingPage)),
    (r"/validation", pyForms.tornadoHandler(validationPage)),
    (r"/dropdown", pyForms.tornadoHandler(dropdownPage)),
    (r"/repeaterValidators", pyForms.tornadoHandler(repeaterValidatorsPage)),
    (r"/file", pyForms.tornadoHandler(filePage)),
])

portNumber = sys.argv[1] if len(sys.argv) > 1 else 8888
application.listen(portNumber)
tornado.ioloop.IOLoop.instance().start()




