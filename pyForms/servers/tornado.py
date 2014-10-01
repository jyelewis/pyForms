import binascii
import tornado.web

import pyForms.network

class Request(pyForms.network.Request):
	@classmethod
	def fromTornado(cls, tornadoObj):
		request = cls()

		#these are taking the same feed. Which has all arguments, fix when smarter
		allArgs = {}
		for key in tornadoObj.request.arguments:
			#this cannot be efficent
			allArgs[key] = tornadoObj.request.arguments[key][0].decode("utf-8")

		request.get  = allArgs
		request.post = allArgs

		#request.url = tornadoObj.static_url
		return request


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






