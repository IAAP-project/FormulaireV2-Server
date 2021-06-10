from Form import Form
from FormWebManager import FormWebManager
from RadioInput import RadioInput
from TextInput import TextInput

F = Form("formtest")
F.addInput(TextInput("Age"))
F.addInput(TextInput("Nom"))
F.addInput(TextInput("Prénom"))
F.addInput(RadioInput("Genre"))
manager = FormWebManager(F)
manager.createServer()



