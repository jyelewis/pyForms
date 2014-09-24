allControls = {}

def registerControl(controlName, control):
	if controlName in allControls:
		raise Exception(controlName + "is already regestered")
	allControls[controlName] = control


#register controls
import pyForms.controls.date
registerControl("date", pyForms.controls.date.Control)