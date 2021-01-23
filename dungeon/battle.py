from creature import Creature

class Battle:
    
    def __init__(self,creature1,creature2):
        self.creature1 = creature1
        self.creature2 = creature2
        
    def fight(self):
        while self.creature1.alive() and self.creature2.alive():
            creature1_attack_strength = self.creature1.attack_strength()
            creature2_attack_strength = self.creature2.attack_strength()
            #print(f"{self.creature1.name} attack strength is {creature1_attack_strength}!")
            #print(f"{self.creature2.name} attack strength is {creature2_attack_strength}!")
            if creature1_attack_strength > creature2_attack_strength:
                self.creature2.wounded()
            elif creature1_attack_strength < creature2_attack_strength:
                self.creature1.wounded()
                
        if self.creature1.alive():
            print(f"{self.creature1.name} emerges victorious!")
            return True
        else:
            print(f"{self.creature2.name} emerges victorious!")    
            return False