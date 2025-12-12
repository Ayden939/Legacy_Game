import random

class Skeleton:

    def __init__(self):
        self.health = 100
        self.strength = 15

    def attack(self, target):
        strike = self.strength + random.randint(1,10)
        print(f"Skeleton attacks {target.name} for {strike} damage!")
        target.incoming_damage(strike)
    
    def incoming_damage(self, damage):
        print(f"Skeleton takes {damage} damage!")
        self.health = self.health - damage
        if(self.health < 0):
            self.health = 0
    
    