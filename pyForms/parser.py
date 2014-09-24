import codecs
import html
import re
from html.parser import HTMLParser

import pyForms.controlManager

class CustomHTMLParser(HTMLParser):
	def __init__(self):
		super().__init__()
		self.depth = 0
		self.curTag = None
		self.tags = []
		self.splitData = None
		self.selfClosingTags = """
area
base
br
col
command
embed
hr
img
input
keygen
link
meta
param
source
track
wbr
		""".split("\n")
		

	def reset(self):
		super().reset()
		self.interesting = re.compile('[<]') #we dont want the default amperstand the the 'intersting' re finds

	def handle_starttag(self, tag, attrs):

		if not self.splitData:
			self.splitData = self.rawdata.split("\n")

		if self.curTag != None and self.curTag['startContentsPos'] == None:
			self.curTag['startContentsPos'] = self.getpos()
		
		self.depth += 1
		if self.depth == 1:
			self.curTag = {
				'name': tag
				,'attrs': attrs
				,'startContentsPos': None
				,'endContentsPos': None
				,'innerHTML': None
				,'isSelfClosing': None
			}
		if tag in self.selfClosingTags:
			self.handle_endtag(tag, True)

	def handle_endtag(self, tag, isHandlingSelfClosing = False):
		if isHandlingSelfClosing ^ (tag in self.selfClosingTags):
			return

		self.depth -= 1

		if self.depth == 0:
			self.curTag['endContentsPos'] = self.getpos()

			if isHandlingSelfClosing:
				self.curTag['isSelfClosing'] = True
			else:
				if self.curTag['startContentsPos'] is None:
					self.curTag['startContentsPos'] = self.curTag['endContentsPos']
				self.curTag['isSelfClosing'] = False
				start = self.curTag['startContentsPos']
				end = self.curTag['endContentsPos']
				dataRows = self.splitData[start[0]-1:end[0]]
				dataRows[0] = dataRows[0][start[1]:]
				if start[0] == end[0]: #remember that this row has already had some content lopped off, account
					dataRows[-1] = dataRows[-1][:end[1]-start[1]]
				else:
					dataRows[-1] = dataRows[-1][:end[1]]

				self.curTag['innerHTML'] = "\n".join(dataRows)

			if 'server' in dict(self.curTag['attrs']):
				self.tags.append(pyForms.controlManager.allControls[self.curTag['name']](self.curTag))
			else:
				self.tags.append(GenericCtrl(self.curTag))
			self.curTag = None

	def handle_data(self, data):
		if self.curTag != None and self.curTag['startContentsPos'] == None:
			self.curTag['startContentsPos'] = self.getpos()

		if self.depth == 0:
			self.tags.append(TextCtrl(data))

	def handle_comment(self, comment):
		if self.depth == 0:
			self.tags.append(TextCtrl("<!--" + comment + "-->"))

	def handle_decl(self, decl):
		if self.depth == 0:
			self.tags.append(TextCtrl("<!" + decl + ">"))



class GenericCtrl():
	def __init__(self, objData):
		self.name = objData['name']
		self.attrs = objData['attrs']
		self.isSelfClosing = objData['isSelfClosing']
		if not self.isSelfClosing:
			self.innerHTML = objData['innerHTML']
			
			self.children = parse(self.innerHTML)

	def render(self):

		strContents  = '<' + self.name
		for attr in self.attrs:
			if attr[1] is not None:
				strContents += ' ' + attr[0] + '="' + html.escape(attr[1]) + '"'
			else:
				strContents += ' ' + attr[0] + '="' + html.escape(attr[0]) + '"'

		if self.isSelfClosing:
			strContents += ' />'
		else:
			strContents += '>'
			for child in self.children:
				strContents += child.render()
			strContents += "</" + self.name + ">"
		
		return strContents

class TextCtrl():
	def __init__(self, text):
		self.text = text

	def render(self):
		return self.text

def parse(html):
	parser = CustomHTMLParser()
	parser.feed(html)
	#create objects from tags
	return parser.tags
