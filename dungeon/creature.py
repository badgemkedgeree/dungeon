import random

class Creature:

    def __init__(self, identifier, skill,stamina,name):
        self.identifier = identifier
        self.skill = random.randint(skill//1.5,skill)
        self.stamina = stamina
        self.name = name
        print(f"{self.name} has skill {self.skill}")
         
    def attack_strength(self):
        return self.skill + random.randint(1,12)
    
    def wounded(self):
        self.stamina -= 2
        print(f"{self.name} was wounded for 2 stamina!\nStamina is now {self.stamina}!")
    
    def alive(self):
        return self.stamina > 0
    
class Player(Creature):
    
    def __init__(self,name):
        self.skill = 6 + random.randint(1,6)
        self.stamina = 12 + random.randint(1,12)
        self.name = name
   
