class Character():
    def __init__(self, name, health, position):
        self.name = name
        self.health = health
        self.position = position


class Sentry(Character):
    def __init__(self, dialogue):
        super().__init__("Sentry", 100, None)
        self.dialogue = dialogue
    
    def speak(self):
        print("The sentry says: ", self.dialogue)


class Player(Character):
    def __init__(self, name, health, inventory, position):
        super().__init__(name, health, position)
        self.inventory = inventory
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
    
    