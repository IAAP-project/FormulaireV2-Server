class BoxChoice:
    def __init__(self, name):
        self.name = name
        self.selected = False

    def getName(self):
        return self.name

    def select(self):
        self.selected = True

    def deselect(self):
        self.selected = False
