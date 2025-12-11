class Skeleton:

    def __init__(self):
        self.health = 100
        self.strength = 15

    def attack(self, target):
        print(f"Skeleton attacks {target.name} for {self.strength} damage!")
        target.incoming_damage(self.strength)
    
    def incoming_damage(self, damage):
        print(f"Skeleton takes {damage} damage!")
        self.health = self.health - damage
        if(self.health < 0):
            self.health = 0
    
    