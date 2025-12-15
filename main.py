
from character import Character
from enemy import Skeleton
from database import log
import database


hero = Character("Lady Samantha Rostnovak", 1)
floor = 0
retreat = False

print("""The towns greatest hero, Lady Samantha Rostnovak, enters the dungeon. Little is known about the dungeon except
that it has been around long before any person had settled there. Many have dove in to explore the depths, but most have fallen,
and none have gone very far. There are a hundreed floors, and a long adventure for our courageous hero.""")


while floor < 10 and not retreat:
    floor = floor + 1
    print(f"Floor: {floor}")
    enemy = Skeleton()

    while hero.health > 0 and enemy.health > 0:

        choice =  input("Please choose attack, retreat, or heal:    ")
        if(choice == "attack"):
            hero.attack(enemy)
            print(f"Enemy hp: {enemy.health}")
            if(enemy.health <= 0):
                print("Enemy defeated!")
                log("Lady Samantha Rostnovak", hero.generation, "Killed Enemy", 0, floor)
                break
            enemy.attack(hero)
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
        
        else:
            print("You must attack, retreat, or heal:   ")
    
        

print("Congrats you win great job!")

database.con.close()