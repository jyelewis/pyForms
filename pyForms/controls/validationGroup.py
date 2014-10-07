import random

import pyForms.ControlBase
import pyForms.parser
import pyForms.controls.Button

class Control(pyForms.ControlBase.Base):
	def __init__(self, obj):
		super().__init__(obj)
		self.validationGroupID = random.randint(1000,9999)



	def parentConfigureFunc(self, ctrlToConfigure):
		ctrlToConfigure.autoPostBackFunction = "pyForms_validate_"+str(self.validationGroupID)+"(event, true);"
		if ctrlToConfigure.id is not None:
			self.allControls[ctrlToConfigure.id] = ctrlToConfigure

		if type(ctrlToConfigure) is pyForms.controls.Button.Control:
			self.buttons.append(ctrlToConfigure)

		if issubclass(ctrlToConfigure.__class__, pyForms.validators.Base.Class):
			self.validators.append(ctrlToConfigure)

	def configureControls(self):
		#reset
		self.allControls = {}
		self.validators = []
		self.buttons = []


		#collect references to all controls
		for child in self.children:
			child.parentConfigure(self.parentConfigureFunc) #calls this function down the tree

		#give each validator its controls
		for validator in self.validators:
			if validator.controlID is not None and validator.control is None:
				try:
					validator.control = self.allControls[validator.controlID]
				except:
					raise Exception("Control not found when binding validator controls")

		#add the validate handlers to buttons
		for button in self.buttons:
			#if 'onclick' in button.attributes:
			#	button.attributes['onclick'] += "pyForms_validate_"+str(self.validationGroupID) + "(event);"
			#else:
			button.attributes['onclick'] = "pyForms_validate_"+str(self.validationGroupID) + "(event);"

	def render(self):
		self.configureControls()
		
		#add the javascript
		javascript = """
			<script type="text/ecmascript">
				function pyForms_validate_"""+str(self.validationGroupID)+"""(e, postback) {
				e = e || window.event;
				hasError = false;
		"""
		for validator in self.validators:
			validator.attributes['id'] = validator.control.attributes['id'] + "_validator"
			if not validator.hasInited:
				validator.initValidator()
			javascript += """if (function() { """ + validator.clientCode + """}()) {
			document.getElementById('""" + validator.attributes['id'] + """').style.display = "";
				if (e.preventDefault) { e.preventDefault(); }
				hasError = true;
			} else {
				document.getElementById('""" + validator.attributes['id'] + """').style.display = "none";
			}
			if (postback && !hasError){
				pyForms_postback();
			}
			"""

		javascript += "} </script>"

		return javascript + self.innerHTML
