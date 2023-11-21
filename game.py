import random


class Card:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class AttackCard(Card):
    def __init__(self, name, description, damage):
        super().__init__(name, description)
        self.damage = damage

    def play(self, target,player):
        target.take_damage(self.damage)

class HealCard(Card):
    def __init__(self, name, description, healing):
        super().__init__(name, description)
        self.healing = healing

    def play(self, target,player):
        target=player
        target.take_healing(self.healing)
        print(f"{target.name} a été soigné de {self.healing} points de vie.")


class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if self.cards:
            return self.cards.pop(0)
        else:
            print("Le deck est vide.")
            return None

class Character:
    def __init__(self, name, max_hp):
        self.name = name
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.deck = Deck()

    def take_damage(self, damage):
        self.current_hp -= damage
        if self.current_hp < 0:
            self.current_hp = 0

    def take_healing(self, healing):
        self.current_hp += healing
        if self.current_hp > self.max_hp:
            self.current_hp = self.max_hp
    
    def is_alive(self):
        return self.current_hp > 0

class Enemy:
    def __init__(self, name, max_hp,attack):
        self.name = name
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.ennemy_attack = attack

    def take_damage(self, damage):
        self.current_hp -= damage
        if self.current_hp < 0:
            self.current_hp = 0

    def take_healing(self, healing):
        self.current_hp += healing
        if self.current_hp > self.max_hp:
            self.current_hp = self.max_hp
    
    def is_alive(self):
        return self.current_hp > 0

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, max_hp=30)

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, max_hp=25)

class Thief(Character):
    def __init__(self, name):
        super().__init__(name, max_hp=28)

warrior = Warrior("Aragorn")
mage = Mage("Gandalf")
thief = Thief("Legolas")

if __name__ == "__main__":
    warrior.deck.add_card(AttackCard("Coup d'Épée", "Une attaque puissante avec une épée", damage=10))
    mage.deck.add_card(HealCard("Sort de Guérison", "Soigne le personnage", healing=8))
    thief.deck.add_card(AttackCard("Frappe Sournoise", "Une attaque furtive", damage=12))

    dragon = Enemy("Dragon", max_hp=50)

    warrior.deck.draw_card().play(dragon)
    mage.deck.draw_card().play(dragon)

    dragon.take_damage(15)
    thief.take_damage(8)

    print(f"{warrior.name}: {warrior.current_hp}/{warrior.max_hp} HP")
    print(f"{mage.name}: {mage.current_hp}/{mage.max_hp} HP")
    print(f"{thief.name}: {thief.current_hp}/{thief.max_hp} HP")
    print(f"{dragon.name}: {dragon.current_hp}/{dragon.max_hp} HP")
