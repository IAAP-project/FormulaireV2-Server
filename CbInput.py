from Input import Input


class CbInput(Input):
    def __init__(self, name):
        super().__init__(name)
        self.values = []

