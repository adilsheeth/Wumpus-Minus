
class Item():
    def __init__(self, name, description, uses):
        self.name = name
        self.description = description
        self.uses = uses
    
    def get_name(self):
        return self.name