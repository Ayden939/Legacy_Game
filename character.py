"""
Defines main player character and actions.
Will be expanded to help manage character generations and inventory
"""


import random

class  Character:


    def __init__(self, name, generation):
        self.name = name
        self.floor = 1
        self.health = 100
        self.strength = 20
        self.generation = generation
    

    def incoming_damage(self, damage):
        print(f"{self.name} takes {damage} damage!")
        self.health = self.health - damage
        if self.health < 0:
            self.health = 0
    

    def attack(self, target):
        strike = self.strength + random.randint(1,5)
        print(f"{self.name} attacks skeleton for {strike} damage!")
        target.incoming_damage(strike)

    def heal(self):
        if self.health < 100:
            amount = random.choice([5,10,15,20])
            if self.health + amount < 100:
                self.health = self.health + amount
                print(f"{self.name} gains {amount} health!")
                damage = random.choice([0, 10, 15])
                self.incoming_damage(damage)
            else:
                difference = 100 - self.health
                self.health = 100
                print(f"{self.name} gains {difference} health!")
                damage = random.choice([0, 10, 15])
                self.incoming_damage(damage)
        else:
            print(f"{self.name}'s health is already full!")