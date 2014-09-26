import tornado.web

import pyForms.network

class Request(pyForms.network.Request):
	@classmethod
	def fromTornado(cls, tornadoObj):
		request = cls()
		#print(dir(tornadoObj))
		#print(tornadoObj.get_arguments())
		request.url = tornadoObj.static_url
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
			self.get(self)

	return pyFormsTornadoRequestHandler






