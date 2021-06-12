class Input(object):
    def __init__(self, name, id):
        self.name = name
        self.id=id

    def saisieInput(self, value, param):
        return True

    def getValue(self):
        return ""

    def getId(self):
        return self.id

    def getName(self):
        return self.name