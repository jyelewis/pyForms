import html
import pyForms.parser
class Base:
	def __init__(self, ctrlData):
		#total primatives, no dependencies
		self.rawInnerHTML = ctrlData['innerHTML']
		self.attributes = dict(ctrlData['attrs'])
		self.tagname = ctrlData['name']

		#configure ID
		self.id = None
		if 'id' in self.attributes:
			self.id = self.attributes['id']

		#link pageInstance (depends: ID)
		self.pageInstance = ctrlData['pageInstance']
		self.pageInstance.registerControl(self)

		#process children elements (depends: pageInstance)
		if self.rawInnerHTML:
			self.children = pyForms.parser.parse(self.rawInnerHTML, self.pageInstance)
		else:
			self.children = []

		#cashe vars
		self._innerHTML = None


		#generic attributes of all controls

		#visible - shows or hides a control
		self.visible = True
		if 'visible' in self.attributes:
			self.visible = (self.attributes['visible'].lower() == "true")
			del self.attributes['visible']


		
	#TODO: this property cant use +=, should be able to
	@property
	def innerHTML(self):
		if self._innerHTML is None:
			self._innerHTML = "".join([x.render() for x in self.children])
		return self._innerHTML

	@innerHTML.setter
	def innerHTML(self, newHTML): #do this via property when youre smart enough to
		#remove references to old children
		for child in self.children:
			if child.id is not None:
				del self.pageInstance.controls[child.id]
		self.children = pyForms.parser.parse(newHTML, self.pageInstance)
		self._innerHTML = None #remove cashe

	#control event functions
	def onRequest(self):
		for child in self.children:
			child.onRequest() #forward event down the tree

	def fireEvents(self):
		for child in self.children:
			child.fireEvents() #forward event down the tree

	def getEventHandler(self, eventName):
		if self.id is None or self.pageInstance.controller is None:
			return None
		handlerName = self.id + "_" + eventName
		handler = getattr(self.pageInstance.controller, handlerName, None)
		if callable(handler):
			def callHandler(*args):
				args = list(args)
				args.insert(0, self.pageInstance.controlsReferenceObj)
				handler(*args)
			return callHandler
		else:
			return None

	def render(self):
		if not self.visible:
			return ""
		strContents  = '<' + self.tagname
		for attr in self.attributes:
			if attr == "server":
				continue #dont add the server attribute
			value = self.attributes[attr] #TODO: There is a way to properly enumerate keys + values
			if value is not None:
				strContents += ' ' + str(attr) + '="' + html.escape(str(value)) + '"'
			else:
				strContents += ' ' + str(attr) + '="' + html.escape(str(value)) + '"'

		if self.isSelfClosing:
			strContents += ' />'
		else:
			strContents += '>'
			for child in self.children:
				strContents += child.render()
			strContents += "</" + self.tagname + ">"
		
		return strContents




