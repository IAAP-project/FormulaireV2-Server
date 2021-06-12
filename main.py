from BoxChoice import BoxChoice
from Form import Form
from FormWebManager import FormWebManager
from RadioInput import RadioInput
from TextInput import TextInput



manager = FormWebManager("formtest", "")
manager.getForm().addInput(TextInput("Prénom", "prenom"))
radio=RadioInput("Genre", "genre")
radio.addChoice(BoxChoice("Homme","male"))
radio.addChoice(BoxChoice("Femme","female"))
manager.getForm().addInput(radio)

manager.getForm().start()
manager.createServer()



