from Input import Input


class TextInput(Input, object):
    def __init__(self, name):
        super(TextInput, self).__init__(name)
        self.text = ""

    def saisieInput(self,value):
        self.text = value
        return True


