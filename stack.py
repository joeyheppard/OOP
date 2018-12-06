class Queue():
    #create stack object
    def__init__(self):
    self.items = []

    def isEmpty(self):
        # return a booleam
        return self.items == []

def push(self, item):
    self.items.append(item)


estelle = Stack()

Queue.push('bork')
print (Queue.isEmpty())

import random
#create pokemon class
class Pokemon():
    def __init__(self, health, attack, name): #initialize pokemon
    #define the attributes of the pokemon
        self.health = health
        self.attack = attack
        self.name = name
        #create function to attack
    def attack(self):
        #if/else or hash w type attacks
        pass
    def battle(self, other):
        #create a function for battle
        print(self.name, 'is in a fight with', other.name)
        #printing the pokemon based off its attributes
        #get user input for attacks
        pick_attack = input('which attack? push or or punch?')

        if pick_attack == 'punch':
            attack = random.randint(15,40)
        else:
            attack = random.randint(0,35)
        #attack on other change hp
        other.health = other.health - attack
        print(self.name, 'did', attack, 'damage to', other.name)
        print(other.name, 'has', other.hp, 'health left')
        #check if other is not knocked out
        if other.hp > 0:
            return(other.battle(self))
        else:
            print(self.name, 'won')

#class ends
#instance of Pokemon
charzard = Pokemon(200,50,'chazard')
 ditto = Pokemon(200,50, 'Ditto')
charzard.battle(ditto)
