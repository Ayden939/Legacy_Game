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
        print(f"{self.name} attacks skeleton for {self.strength} damage!")
        target.incoming_damage(self.strength)

    def heal(self, amount):
        self.health = self.health + amount