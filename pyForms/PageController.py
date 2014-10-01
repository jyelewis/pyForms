class PageController:
	def __init__(self, page):
		self.page = page

	def onInit(self, ctrls):
		pass

	def onLoad(self, ctrls):
		pass

	def onPrerender(self, ctrls):
		pass

	def setHTMLFile(self):
		raise NotImplementedError("setHTMLFile is not implemented")

	def pageCode(self):
		if not hasattr(self, 'htmlFile'):
			self.setHTMLFile()

		if not hasattr(self, 'htmlFile'):
			raise Exception("setHTMLFile didn't set self.htmlFile !")

		file = open(self.htmlFile, 'r')
		retValue = file.read()
		file.close()
		return retValue