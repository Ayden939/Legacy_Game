
from character import Character
from enemy import Skeleton, Goblin, Phantom
from database import log
import database
import random
from equipment import Sword, Shield
from loot import loot_drop

hero = Character("Lady Samantha Rostnovak", 1)
floor = 0
retreat = False

print("""The towns greatest hero, Lady Samantha Rostnovak, enters the dungeon. Little is known about the dungeon except
that it has been around long before any person had settled there. Many have dove in to explore the depths, but most have fallen,
and none have gone very far. There are a hundreed floors, and a long adventure for our courageous hero.""")


while floor < 10 and not retreat:
    floor = floor + 1
    print(f"Floor: {floor}")
    enemy = random.choice([Skeleton(), Goblin(), Phantom()])
    print(f"A {enemy.name} blocks Lady Samantha's path.")

    while hero.health > 0 and enemy.health > 0:
        choice =  input("Please choose attack, retreat, or heal:    ")
        if(choice == "attack"):
            hero.attack(enemy)
            if(enemy.health <= 0):
                print("Enemy defeated!")
                item = loot_drop(enemy.rarity, hero)
                if item:
                    hero.equip(item, enemy)
                log("Lady Samantha Rostnovak", hero.generation, "Killed Enemy", 0, floor)
                break
            enemy.attack(hero)
            print(f"Enemy hp: {enemy.health}")
            print(f"Hero hp: {hero.health}")

            if(hero.health <= 0):
                print("Defeated")
                break
            
        elif(choice == "retreat"):
            print(f"Lady Samantha Rostnovak has left the dungeon")
            retreat = True
            break

        elif(choice == "heal"):
            hero.heal()
            print(f"Hero hp: {hero.health}")
            print(f"Enemy hp: {enemy.health}")
        
        else:
            print("You must attack, retreat, or heal:   ")
    
    if(hero.health <= 0):
        break


if(floor > 10):
    print(f"{hero.name} has beat the dungeon!")

database.con.close()