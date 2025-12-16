"""
Defines main player character and actions.
Will be expanded to help manage character generations and inventory
"""


import random

class  Character:


    def __init__(self, name, generation, weapon = None, armor = None):
        self.name = name
        self.floor = 1
        self.health = 100
        self.strength = 20
        self.generation = generation
        self.weapon = weapon
        self.armor = armor
    

    def incoming_damage(self, damage):

        if(self.armor):
            if(damage - self.armor.defense > 0):
                damage = damage - self.armor.defense
            else:
                damage = 0

        print(f"{self.name} takes {damage} damage!")
        self.health = self.health - damage
        if self.health < 0:
            self.health = 0
    

    def attack(self, target):

        if(self.weapon):
            weapon_attack = self.weapon.attack
        else:
            weapon_attack = 0

        strike = self.strength + random.randint(1,5) + weapon_attack
        print(f"{self.name} attacks {target.name} for {strike} damage!")
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


    def equip(self, equipment, enemy):
        print(f"{enemy.name} has dropped {equipment.name}")
        choice = ""

        while choice != "yes" and choice != "no":
            choice = input("Would you like to equip? ").strip().lower()
            if(choice == "yes"):
                if(equipment.type == "weapon"):
                    self.weapon = equipment
                else:
                    self.armor = equipment

                print(f"{self.name} equipped {equipment.name}!")


            elif(choice == "no"):
                print(f"{self.name} continues on...")
            else:
                print(f"Please enter yes or no: ")
