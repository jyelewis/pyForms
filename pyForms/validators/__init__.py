import pyForms.controlManager


from  pyForms.validators import required
pyForms.controlManager.registerControl("validator:required", required.Control)