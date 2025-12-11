class  Character:


    def __init__(self, name, generation):
        self.name = name
        self.floor = 1
        self.health = 100
        self.strength = 20
        self.generation = generation
    

    def incoming_damage(self, damage):
        self.health = self.health - damage
        if self.health < 0:
            self.health = 0
    

    def attack(self, target):
        target.incoming_damage(self.strength)

    def heal(self, heal):
        self.health = self.health + heal