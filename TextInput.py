from Input import Input


class TextInput(Input):
    def __init__(self, name):
        super().__init__(name)
        self.text = ""

    def saisieInput(self,value):
        self.text= value
        return True


