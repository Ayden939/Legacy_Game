class skeleton:

    def __init__(self):
        self.health = 100
        self.strength = 15

    def attack(self):
        character.incoming_damage(self.strength)
    
    def incoming_damage(self, damage):
        self.health = self.health - damage
        if(health < 0):
            health = 0
    
    