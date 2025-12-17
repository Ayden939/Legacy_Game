"""
label = tk.label(root, text = 'Some Text')
label.pack

Label will display text/images
root is where tkinter places it
.pack(), .grid(), .place() actually places it

""""

import tkinter as tk
from character import Character
from enemy import Skeleton, Goblin, Phantom
from database import log
import database
import random
from equipment import Sword, Shield
from loot import loot_drop

# Game objects
hero = Character("Lady Samantha Rostnovak", 1)
floor = 0
retreat = False

# Tkinter GUI setup
root = tk.Tk()      # This creates the window, and root.title just applies the title to it
root.title("Legacy Game")



# Info Labels
floor_label = tk.label(root, text=f"Floor: {floor}")
floor_label.pack()

hero_label = tk.label(root, text=f"{hero.name} HP: {hero.health}")
hero_label.pack()

enemy_label = tk.label(root, text=f"{enemy.name} Enemy HP: {enemy.health}")
enemy_label.pack()

output_label = tk.label(root, text = "")
output_label.pack()



def attack():
    damage = hero.attack(enemy)
    update_labels(f"{hero.name} attacks {enemy.name} for {damage} damage!")
    if(enemy.health <= 0):
        update_labels("Enemy defeated!")
        #item = loot_drop(enemy.rarity, hero)
        #if item:
        #    hero.equip(item, enemy)
        log("Lady Samantha Rostnovak", hero.generation, "Killed Enemy", 0, floor)
        new_floor()
        return
    enemy.attack(hero)
    update_labels(f"{hero.name} HP: {hero.health}\n{enemy.name} HP: {enemy.health}")

    if(hero.health <= 0):
        update_labels("Defeated")
        disable_buttons()

    
def heal():
    healed, damage = hero.heal()
    update_labels(f"Hero gained {healed} health and was attacked for {damage} damage!")
    update_labels(f"Hero hp: {hero.health}")
    update_labels(f"Enemy hp: {enemy.health}")

def retreat():
    update_labels(f"{hero.name} has left the dungeon")
    disable_buttons()


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

            
        elif(choice == "retreat"):
            print(f"Lady Samantha Rostnovak has left the dungeon")
            retreat = True
            break

        
        else:
            print("You must attack, retreat, or heal:   ")
    
    if(hero.health <= 0):
        break


if(floor > 10):
    print(f"{hero.name} has beat the dungeon!")

database.con.close()