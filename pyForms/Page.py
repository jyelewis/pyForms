import pyForms.parser

class Page():
	def __init__(self, code, clsController = None):
		self.code = code
		#self.clsController
		#self.controller = clsController()

		self._tree = None

	@property
	def tree(self):
		if not self._tree:
			self._tree = pyForms.parser.parse(self.code)
		return self._tree


	def render(self):
		return "".join([x.render() for x in self.tree])



#before: tags dont reexecute between renders
#after cant have dynamic properties
#or we could have two types of tags...