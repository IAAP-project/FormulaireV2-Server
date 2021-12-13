import time

from Input import Input


class Form:
    def __init__(self, name, manager):
        self.name = name
        self.manager = manager
        self.inputs = []
        self.editedInputs = []
        self.currentInputIndex = 0

    def sayNextInput(self):
        input = self.inputs[self.currentInputIndex]
        self.manager.sayNextInput(input)

    def sayEndInput(self):
        input = self.inputs[self.currentInputIndex]
        self.manager.sayEndInput(input)

    def sayEndForm(self):
        self.manager.sayEndForm()

    def saisie(self,value):
        if self.currentInputIndex >= len(self.inputs):
            return

        input = self.inputs[self.currentInputIndex]
        if input.saisieInput(value, "saisieOrale"):
            #Do end check
            self.editedInputs += [input]
            self.sayEndInput()
            self.currentInputIndex += 1
            if self.currentInputIndex == len(self.inputs):
                time.sleep(2)
                self.sayEndForm()
            else:
                self.sayNextInput()

    def saisieById(self,value,id):
        for i in range(len(self.inputs)):
            if id == self.inputs[i].getId():
                input=self.inputs[i]
                if input.saisieInput(value, "saisieEcrite"):
                    self.editedInputs += [input]

    def start(self):
        if len(self.inputs) > 0:
            self.sayNextInput()

    def retreiveEditedInputs(self):
        inputs = self.editedInputs
        self.editedInputs = []
        return inputs

    def addInput(self,input):
        self.inputs += [input]

    def getInput(self, inputId) -> Input:
        for input in self.inputs:
            if input.getId() == inputId:
                return input
        raise LookupError("Champ non trouvé!")



