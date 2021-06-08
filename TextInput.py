import Input


class TextInput(Input):
    def __init__(self, name):
        super.__init__(self, name)
        self.text = ""

    def saisieInput(self,value):
        self.text= value
        return True


