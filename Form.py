class Form:
    def __init__(self):
        self.inputs = []
        self.currentInputIndex = 0

    def saisie(self,value):
        input = self.inputs[self.currentInputIndex]
        if input.saisieInput(value):
            #Do end check
            self.currentInputIndex += 1
