class Equipment:
    
    def __init__(self, name, defense, attack, type):
        self.name = name
        self.defense = defense
        self.attack = attack
        self.type = type


class Sword(Equipment):
    def __init__(self):
        super().__init__("Rusty Sword", 0, 5, "weapon")

class Shield(Equipment):
    def __init__(self):
        super().__init__("Worn Shield", 5, 0, "armor")
