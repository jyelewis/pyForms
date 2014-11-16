import random
import re
import sys

import pyForms.parser
import pyForms.auth

class Page():
	def __init__(self, clsController, requireAuthentication = False):
		self.clsController = clsController
		self.requireAuthentication = requireAuthentication
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

			#templating
			#controller.template is a reference to the controller class
			#instance.templateInstance is a pageInstance
			if instance.controller.template is not None:
				instance.templateInstance = PageInstance(template_Page(instance.controller.template, instance))



		#do the handling
		if not self.requireAuthentication or pyForms.auth.authenticateRequest(request, response, instance):
			if instance.templateInstance:
				pageResponseCode = instance.templateInstance.renderRequest(request, response)
			else:
				pageResponseCode = instance.renderRequest(request, response)
			if not response.isLocked:
				response.write(pageResponseCode)
				response.end()
		



class template_Page(Page):
	def __init__(self, clsController, innerPageInstance):
		super().__init__(clsController)
		self.innerPageInstance = innerPageInstance

#------------------------------------------------------------------------------------


class PageInstance():
	def __init__(self, page):
		if isinstance(page, template_Page):
			#have the template use the same page instance id as the content, so postbacks work
			self.id = page.innerPageInstance.id
		else:
			self.id = str(random.randint(100000, 999999))
		self.page = page
		self.controller = None
		self.controlsReferenceObj = controlsReference(self)
		self.templateInstance = None

		self.controls = {}

		#init controller class
		if self.page.clsController is not None:
			self.controller = page.clsController(self)

		#get the code
		self.code = self.controller.pageCode()

		self.tree = pyForms.parser.parse(self.code, self)

		self.hasInited = False

	def renderRequest(self, request, response):
		#page life cycle all happens here

		#store request so it can be accessed by controls and controller class
		self.request = request
		self.response = response
		
		self.controller.request = request

		if not self.hasInited:
			#life cycle 1 - init controller
			self.controller.onInit(self.controlsReferenceObj)
			self.hasInited = True
			

		#2 - pass request to each control to update themselves
		for control in self.tree:
			control.onRequest()

		#3 - controller load event
		self.controller.onLoad(self.controlsReferenceObj)

		#4 - fire control events
		for control in self.tree:
			control.fireEvents()

		#5 - controller pre-render event
		self.controller.onPrerender(self.controlsReferenceObj)

		#6 - render page and write response
		return self.render()

		#done with the request, dont keep it around
		self.request = None
		self.controller.request = None

	def registerControl(self, control):
		if control.id is not None:
			if control.id in self.controls:
				raise Exception("ID registered twice!")
			else:
				self.controls[control.id] = control

	#auth methods -----------------------------------------
	
	@property
	def userData(self):
		if 'auth_userdata' in self.request.session:
			return self.request.session['auth_userdata']
		return None

	@property
	def isLoggedIn(self):
		return 'auth_userdata' in self.request.session
	
	#end auth ---------------------------------------------

	def render(self):
		pageCode = "".join([x.render() for x in self.tree])
		
		localVars = dict([(x, getattr(self.controller, x)) for x in dir(self.controller)])
		pageCode = re.sub("{{(.*)}}", lambda match: str(eval(match.group(1), globals(), localVars)), pageCode)

		return pageCode


#------------------------------------------------------------
class controlsReference:
	def __init__(self, pageInstance):
		self.pageInstance = pageInstance

	def __getattr__(self, controlID):
		if controlID in self.pageInstance.controls:
			return self.pageInstance.controls[controlID]
		else:
			return None
