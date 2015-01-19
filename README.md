# pyForms
python implimentation of ASP webforms

PyForms is in essence a HTML parser. It allows custom HTML controls to be written as a python class then used within your HTML source

Eg.
<textbox server id="tbxName" />

An assisoated textbox class is written and bound to the 'textbox' tag.
These controls are held between page actions or 'post backs' allowing for stateful webpages
