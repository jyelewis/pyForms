import pyForms.parser
from pyForms.controlManager import registerControl
from pyForms.customControl import Base as CustomControl


def render(HTMLCode):
	tree = pyForms.parser.parse(HTMLCode)
	return "".join([x.render() for x in tree])