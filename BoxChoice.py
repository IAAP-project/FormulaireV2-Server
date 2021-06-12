class BoxChoice:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.selected = False

    def getName(self):
        return self.name

    def select(self):
        self.selected = True

    def deselect(self):
        self.selected = False

    def getId(self):
        return self.id