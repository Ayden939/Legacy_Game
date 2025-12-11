class Skeleton:

    def __init__(self):
        self.health = 100
        self.strength = 15

    def attack(self, target):
        target.incoming_damage(self.strength)
    
    def incoming_damage(self, damage):
        self.health = self.health - damage
        if(self.health < 0):
            self.health = 0
    
    