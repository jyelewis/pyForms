import pyForms
import cgi

class Controller(pyForms.PageController):
	def setHTMLFile(self):
		self.HTMLFile = "webpages/file.html"
		
	def onInit(self, ctrls):
		self.latestFile = None

	def fileUpload_upload(self, ctrls):
		self.latestFile = ctrls.fileUpload.file

	@property
	def fileContents(self):
		return cgi.escape(self.latestFile['contents'].decode('utf-8')) if self.latestFile else ""