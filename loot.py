import random
from equipment import Sword, Shield

def loot_drop(rarity, hero):
    
    possible_drops = []
    weights = []

    if hero.weapon is None:
        possible_drops.append(Sword())
        weights.append(.4)

    if hero.armor is None:
        possible_drops.append(Shield())
        weights.append(.5)

    possible_drops.append(None)
    weights.append(.1)

    choice = random.choices(possible_drops, weights = weights, k = 1)[0]

    return choice