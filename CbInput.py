from Input import Input


class CbInput(Input, object):
    def __init__(self, name, id):
        super(CbInput, self).__init__(name, id)
        self.values = []

