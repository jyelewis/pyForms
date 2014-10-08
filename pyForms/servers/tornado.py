import binascii
import tornado.web

import pyForms.network

class Request(pyForms.network.Request):
	@classmethod
	def fromTornado(cls, tornadoObj):
		request = cls(tornadoObj)

		#these are taking the same feed. Which has all arguments, fix when smarter
		allArgs = {}
		for key in tornadoObj.request.arguments:
			#this cannot be efficent
			allArgs[key] = tornadoObj.request.arguments[key][0].decode("utf-8")

		allFiles = {}
		for key in tornadoObj.request.files:
			#this cannot be efficent
			file = tornadoObj.request.files[key][0]
			fileDict = {}
			fileDict['contents'] = file['body']
			fileDict['contentType'] = file['content_type']
			fileDict['filename'] = file['filename']
			allFiles[key] = fileDict

		allCookies = {}
		for key in tornadoObj.request.cookies:
			allCookies[key] = tornadoObj.request.cookies[key].value

		request.get  = allArgs
		request.post = allArgs
		request.files = allFiles
		request.cookies = allCookies

		#request.url = tornadoObj.static_url
		return request

	def __init__(self, tornadoObj):
		super().__init__()
		self.tornadoObj = tornadoObj

	def setCookie(self, name, value, args):
		defaultArgs = {
			 'expires': None
			,'domain': None
			,'path': "/"
		}
		args = dict(list(defaultArgs.items()) + list(args.items())) #fill with defaults
		self.tornadoObj.set_cookie(name, value, args['domain'], args['expires'], args['expires'])

	def clearCookie(self, name, domain = None, path = "/"):
		self.tornadoObj.clear_cookie(name, path, domain)



class Response(pyForms.network.Response):
	@classmethod
	def fromTornado(cls, tornadoObj):
		response = cls(tornadoObj)
		return response

	def __init__(self, tornadoObj):
		self.tornadoObj = tornadoObj

	def write(self, content):
		self.tornadoObj.write(content)

	def redirect(self, location):
		print("*redirect called*")
		raise NotImplementedError



def tornadoHandler(page): #returns handler class
	class pyFormsTornadoRequestHandler(tornado.web.RequestHandler):
		def get(self):
			request = Request.fromTornado(self)
			response = Response.fromTornado(self)
			page.handleRequest(request, response)

		def post(self):
			self.get()

	return pyFormsTornadoRequestHandler






