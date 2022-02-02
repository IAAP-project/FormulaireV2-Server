from Input import Input


class RadioInput(Input, object):
    def __init__(self, name, id):
        super(RadioInput, self).__init__(name,id)
        self.choices = []
        self.selectedIndex = -1

    def saisieInput(self, value, param):
        byId = param == "saisieEcrite"
        for i in range(len(self.choices)):
            if (byId and self.choices[i].getId() == value) or ((not byId) and self.choices[i].getName().lower() == value.lower()):
                if self.selectedIndex != -1:
                    self.choices[self.selectedIndex].deselect()
                self.selectedIndex = i
                self.choices[i].select()
                return True
        return False

    def getValue(self):
        if self.selectedIndex != -1:
            return self.choices[self.selectedIndex].getValue()
        return -1

    def addChoice(self, choice):
        self.choices += [choice]





