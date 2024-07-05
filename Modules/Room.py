
class Room:
    def __init__(self, name, id, description, items, links):
        self.name = name
        self.description = description 
        self.items = items
        self.links = links
        self.id = id
    
    def get_name(self):
        return self.name

    def get_description(self):
        return self.description
    
    def set_description(self, description):
        self.description = description

    def get_items(self):
        if self.items == []:
            return []
        else:
            return self.items[0]
    
    def get_links(self):
        return self.links