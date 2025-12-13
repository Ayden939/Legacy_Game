# Plan later to possibly make this a game object, research it

from character import Character
from skeleton import Skeleton

hero = Character("Lady Samantha Rostnovak", 1)
enemy = Skeleton()
floor = 0

print("""The towns greatest hero, Lady Samantha Rostnovak, enters the dungeon. Little is known about the dungeon except
that it has been around long before any person had settled there. Many have dove in to explore the depths, but most have fallen,
and none have gone very far. There are a hundreed floors, and a long adventure for our courageous hero.""")

while hero.health > 0 and enemy.health > 0:

    floor = floor + 1

    print(f"Floor: {floor}")

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
        