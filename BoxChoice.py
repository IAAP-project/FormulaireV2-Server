class BoxChoice:
    def __init__(self, name, id, value):
        self.name = name
        self.id = id
        self.value = value
        self.selected = False

    def getName(self):
        return self.name

    def select(self):
        self.selected = True

    def deselect(self):
        self.selected = False

    def getId(self):
        return self.id

    def getValue(self):
        return self.value