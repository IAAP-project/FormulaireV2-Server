from Input import Input


class TextInput(Input, object):
    def __init__(self, name, id):
        super(TextInput, self).__init__(name,id)
        self.text = ""

    def saisieInput(self, value, param):
        self.text = value
        return True

    def getValue(self):
        return self.text
