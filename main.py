# Plan later to possibly make this a game object, research it

from character import Character
from skeleton import Skeleton

hero = Character("Lady Samantha Rostnovak", 1)
enemy = Skeleton()

while hero.health > 0 and enemy.health > 0:

    choice =  input("Please choose attack, retreat, or heal:    ")
    if(choice == "attack"):
        hero.attack(enemy)
        print(f"Enemy hp: {enemy.health}")
        if(enemy.health <= 0):
            print("Enemy defeated!")
            break
        enemy.attack(hero)
        print(f"Hero hp: {hero.health}")
        if(hero.health <= 0):
            print("Defeated")
            break
        
    elif(choice == "retreat"):
        print(f"{hero.name} has left the dungeon")
        break

    elif(choice == "heal"):
        hero.heal(5)
        print(f"Hero hp: {hero.health}")
    
    else:
        print("You must attack, retreat, or heal:   ")
        