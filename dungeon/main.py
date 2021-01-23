from creature import Creature
from battle import Battle
from location import Location
from creature import Player
from world import World


world1 = World()
print("Please enter your character's name to generate your STATs!")
name = input()
player = Player(name)
print(f"Welcome {player.name},to this perilous journey! You have skill:{player.skill} & stamina:{player.stamina} ")

current_location = world1.get_location("location1")
while player.alive() and current_location is not None:
    print(current_location.description)
    enemy = world1.get_creature(current_location.enemy_identifier)
    if enemy is not None:
        print(f"You are attacked by a {enemy.name} and a battle starts to commence!")
        battle1 = Battle(enemy,player)
        result = battle1.fight()
    current_location = world1.get_location(current_location.next_location_identifier)

if player.alive():
    print("Your have been awarded a trophy of Bravery, lots of gold and a dusty book of spells. Well done.")
    print(f"...and you had {player.stamina} stamina left.")
else:
    print(f"Your journey ends here. You are DEAD, {player.name}")