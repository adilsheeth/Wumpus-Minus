
class Sentry():
    def __init__(self):
        pass


class Player():
    def __init__(self, name, health, inventory, position):
        self.name = name
        self.health = health
        self.inventory = inventory
        self.position = position
        self.boozed = 0
    
    def move(self, new_room):
        self.position = new_room

    def set_boozed(self, boozed):
        self.boozed = boozed
    
    def get_inventory(self):
        return self.inventory

    def get_position(self):
        return self.position
    
    