from Input import Input


class RadioInput(Input):
    def __init__(self, name):
        super().__init__(name)
        self.choices = []
        self.selectedIndex = -1

    def saisieInput(self,value):
        for i in range(len(self.choices)):
            if self.choices[i].getName() == value:
                if self.selectedIndex != -1:
                    self.choices[self.selectedIndex].deselect()
                self.selectedIndex = i
                self.choices[i].select()
                return True
        return False

