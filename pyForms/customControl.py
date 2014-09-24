import pyForms.parser
class Base:
	def __init__(self, ctrlData):
		self.rawInnerHTML = ctrlData['innerHTML']
		self.attributes = dict(ctrlData['attrs'])
		self.tagname = ctrlData['name']

		self._innerHTML = None

	@property
	def innerHTML(self):
		if self._innerHTML is None:
			tree = pyForms.parser.parse(self.rawInnerHTML)
			self._innerHTML = "".join([x.render() for x in tree])
		return self._innerHTML

	def render(self):
		raise NotImplimentedError