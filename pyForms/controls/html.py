import pyForms.CustomControl
import pyForms.parser

class Control(pyForms.CustomControl.Base):
	def __init__(self, obj):
		super().__init__(obj)
		self.isSelfClosing = False

		self.head = findControl(self.children, 'head')
		self.body = findControl(self.children, 'body')

		#wrap the contents of the body inside a form tag
		formTag = pyForms.parser.GenericCtrl({
			'name': "form"
			,'attrs': { 'method': 'POST', 'id': 'pyForms__postbackForm' }
			,'innerHTML': None
			,'pageInstance': self.pageInstance
			,'isSelfClosing': False
		})
		formTag.children = self.body.children
		
		#add a hidden field to the form to identify the page
		hiddenTag = pyForms.parser.GenericCtrl({
			'name': "input"
			,'attrs': {
				 'type': 'hidden'
				,'name': 'pyForms__postbackInstanceID'
				,'value': self.pageInstance.id
			}
			,'innerHTML': None
			,'pageInstance': self.pageInstance
			,'isSelfClosing': True
		})
		formTag.children.insert(0, hiddenTag)

		self.body.children = [formTag]



def findControl(controls, tagName):
	for control in controls:
		if control.tagname == tagName:
			return control



