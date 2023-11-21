import random
from dice import Dice
from character import Warrior, Mage, Thief, Character

if __name__ == "__main__":
    warrior = Warrior("james", 20, 8, 3, Dice(6))
    mage = Mage("elisa", 20, 8, 3, Dice(6))
    thief = Thief("michel", 20, 8, 3, Dice(6))
    
    car: list[Character] = [warrior, mage, thief]
    
    char1 = random.choice(car)
    car.remove(char1)
    char2 = random.choice(car)
    car.remove(char2)
    
    print (char1)
    print (char2)
    print (car)
    
    stats ={
        char1.get_name():0,
        char1.get_name():0,    
    }
    
    for _ in range(100):
        char1.regenerate()
        char2.regenerate()
        
        
        while char1.is_alive() and char2.is_alive():
            char1.attack(char2)
            char2.attack(char1)
            
        if char1.is_alive():
            stats[char1.get_name()] += 1
        else:
            stats[char1.get_name()] += 1