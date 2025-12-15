"""
Defines all enemy types and behavior.
Enemies ineherit from the parent enemy class.
"""


import random

class Enemy:
    def __init__(self, name, strength, health):
        self.name = name
        self.strength = strength
        self.health = health

    def attack(self, target):
        strike = self.strength + random.randint(5,20)
        print(f"{self.name} attacks {target.name} for {strike} damage!")
        target.incoming_damage(strike)
    
    def incoming_damage(self, damage):
        print(f"{self.name} takes {damage} damage!")
        self.health = self.health - damage
        if(self.health < 0):
            self.health = 0
    
    

class Skeleton(Enemy):

    def __init__(self):
        super().__init__("Skeleton", 15, 100)


class Goblin(Enemy):

    def __init__(self):
        super().__init__("Goblin", 20, 90)


class Phantom(Enemy):

    def __init__(self):
        super().__init__("Phantom", 5, 150)

    def attack(self, target):
        strike = self.strength + random.randint(5,20)
        print(f"{self.name} attacks {target.name} for {strike} damage!")
        target.incoming_damage(strike)

        print(f"{self.name} grows stronger...")
        self.strength += 2