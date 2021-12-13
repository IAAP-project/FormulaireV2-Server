from BoxChoice import BoxChoice
from Form import Form
from FormWebManager import FormWebManager
from RadioInput import RadioInput
from TextInput import TextInput



manager = FormWebManager("form_age_du_coeur", "")

manager.getForm().addInput(TextInput("Prénom", "prenom"))

manager.getForm().addInput(TextInput("Age", "age"))

radio=RadioInput("Genre", "genre")
radio.addChoice(BoxChoice("Homme","homme"))
radio.addChoice(BoxChoice("Femme","femme"))
manager.getForm().addInput(radio)

radio=RadioInput("Êtes-vous fumeur?", "fumeur")
radio.addChoice(BoxChoice("Oui","oui"))
radio.addChoice(BoxChoice("Non","non"))
manager.getForm().addInput(radio)

radio=RadioInput("Êtes-vous diabétique?", "diabetique")
radio.addChoice(BoxChoice("Oui","oui"))
radio.addChoice(BoxChoice("Non","non"))
manager.getForm().addInput(radio)

radio=RadioInput("Avez-vous de l'hypertension?", "hypertension")
radio.addChoice(BoxChoice("Oui","oui"))
radio.addChoice(BoxChoice("Non","non"))
manager.getForm().addInput(radio)

radio=RadioInput("Êtes-vous traité pour de l'hypertension?", "traitement_hypertension")
radio.addChoice(BoxChoice("Oui","oui"))
radio.addChoice(BoxChoice("Non","non"))
manager.getForm().addInput(radio)

manager.getForm().addInput(TextInput("Tension", "tension"))

manager.getForm().addInput(TextInput("Taux de cholestérol total", "taux_colesterol"))

manager.getForm().addInput(TextInput("HDL cholestérol", "HDL_colesterol"))

manager.getForm().start()
manager.createServer()



