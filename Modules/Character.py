
class Sentry():
    def __init__(self, dialogue):
        self.dialogue = dialogue
    
    def speak(self):
        print("The sentry says: ", self.dialogue)


class Player():
    def __init__(self, name, health, inventory, position):
        self.name = name
        self.health = health
        self.inventory = inventory
        self.position = position
        self.boozed = 0
        self.enemies_to_kill = 3
    
    def move(self, new_room):
        self.position = new_room

    def set_boozed(self, boozed):
        self.boozed = boozed
    
    def get_enemies_to_kill(self):
        return self.enemies_to_kill
    
    def set_enemies_to_kill(self):
        self.enemies_to_kill -= 1
    
    def get_boozed(self):
        return self.boozed > 0
    
    def get_boozed_value(self):
        return self.boozed
    
    def get_inventory(self):
        return self.inventory

    def get_position(self):
        return self.position
    
    