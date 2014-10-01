import random

import pyForms.parser

class Page():
	def __init__(self, code, clsController = None):
		self.code = code
		self.clsController = clsController

		self.pageInstances = {}

	def handleRequest(self, request, response):
		#check if instance already exists and use that if it does
		instance = None

		#check if post back, loadup instance
		if 'pyForms__postbackInstanceID' in request.post:
			instanceID = request.post['pyForms__postbackInstanceID']
			if instanceID in self.pageInstances:
				instance = self.pageInstances[instanceID]

		#no instance found, create new
		if instance is None:
			instance = PageInstance(self)
			#store for postbacks
			self.pageInstances[instance.id] = instance

		#do the handling
		instance.handleRequest(request, response)




#------------------------------------------------------------------------------------





class PageInstance():
	def __init__(self, page):
		self.id = str(random.randint(100000, 999999))
		self.page = page
		self.controller = None

		self.controls = {}

		#init controller class
		if self.page.clsController is not None:
			self.controller = page.clsController(self)

		self.tree = pyForms.parser.parse(self.page.code, self)

		#life cycle 1 - init controller
		if self.controller:
			self.controller.onInit()

	def handleRequest(self, request, response):
		#page life cycle all happens here

		#store request so it can be accessed by controls and controller class
		self.request = request

		#2 - pass request to each control to update themselves
		for control in self.tree:
			control.onRequest()

		#3 - controller load event
		if self.controller:
			self.controller.onLoad()

		#4 - fire control events
		for control in self.tree:
			control.fireEvents()

		#5 - controller pre-render event
		if self.controller:
			self.controller.onPrerender()

		#6 - render page and write response
		response.write(self.render())

		#done with the request, dont keep it around
		self.request = None

	def registerControl(self, control):
		if control.id is not None:
			if control.id in self.controls:
				raise Exception("ID registered twice!")
			else:
				self.controls[control.id] = control

	def render(self):
		return "".join([x.render() for x in self.tree])



#before: tags dont reexecute between renders
#after cant have dynamic properties
#or we could have two types of tags...