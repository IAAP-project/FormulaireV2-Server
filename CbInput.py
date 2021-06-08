from Input import Input


class CbInput(Input, object):
    def __init__(self, name):
        super(CbInput, self).__init__(name)
        self.values = []

