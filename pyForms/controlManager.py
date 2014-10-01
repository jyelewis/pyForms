allControls = {}

def registerControl(controlName, control):
	controlName = controlName.lower()
	if controlName in allControls:
		raise Exception(controlName + "is already regestered")
	allControls[controlName] = control


#register controls
import pyForms.controls.Textbox
registerControl("Textbox", pyForms.controls.Textbox.Control)

import pyForms.controls.Button
registerControl("Button", pyForms.controls.Button.Control)
#import pyForms.controls.date
#registerControl("date", pyForms.controls.date.Control)