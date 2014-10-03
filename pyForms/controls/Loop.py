import random

import pyForms.CustomControl
import pyForms.parser

class Control(pyForms.CustomControl.Base):
	def __init__(self, obj):
		#obj['customRegisterFunction'] = self.customRegisterFunction
		rawInnerHTML = obj['innerHTML']
		obj['innerHTML'] = None #make sure the children arent processed
		super().__init__(obj)
		self.rawInnerHTML = rawInnerHTML

		self.dataSource = []
		
		self.loops = []

		self.configureLoopHandler = self.getEventHandler("configureLoop")

	def update(self):
		self.loops = []
		controlsDict = {}
		controlsReference = ControlsReference(controlsDict)

		registerID = 1

		def customRegisterFunction(controlToRegister):
			nonlocal registerID
			if controlToRegister.id is not None:
				controlToRegister.attributes['id'] = self.id + "_" + controlToRegister.id + "_" + str(registerID)
				registerID += 1

				controlsDict[controlToRegister.id] = controlToRegister

		for index, item in enumerate(self.dataSource):
			controls = pyForms.parser.parse(self.rawInnerHTML, self.pageInstance, customRegisterFunction)
			self.loops.append((
				 index
				,item
				,controls
				,controlsDict
			))

			if self.configureLoopHandler:
				self.configureLoopHandler(controlsReference, item, index)

	def render(self):
		renderCode = ""
		for loop in self.loops:
			renderCode += "".join([x.render() for x in loop[2]])


		return renderCode


class ControlsReference:
	def __init__(self, controlsDict):
		self.controlsDict = controlsDict

	def __getattr__(self, controlID):
		if controlID in self.controlsDict:
			return self.controlsDict[controlID]
		else:
			return None






