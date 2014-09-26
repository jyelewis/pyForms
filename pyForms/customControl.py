import pyForms.parser
class Base:
	def __init__(self, ctrlData):
		self.rawInnerHTML = ctrlData['innerHTML']
		self.attributes = dict(ctrlData['attrs'])
		self.tagname = ctrlData['name']
		self.children = pyForms.parser.parse(self.rawInnerHTML)
		self.pageInstance = None

		self._innerHTML = None
		

		self.registerChildren()

	def registerChildren(self):
		pass #will register all children to the page obj at some point

	@property
	def innerHTML(self):
		if self._innerHTML is None:
			self._innerHTML = "".join([x.render() for x in self.children])
		return self._innerHTML

	#kinda important one
	def setPageInstance(self, pageInstance):
		self.pageInstance = pageInstance
		for child in self.children:
			child.setPageInstance(pageInstance)

	#control event functions
	def onRequest(self):
		for child in self.children:
			child.onRequest() #forward event down the tree

	def fireEvents(self):
		for child in self.children:
			child.fireEvents() #forward event down the tree

	def render(self):
		raise NotImplimentedError




