from __future__ import annotations
import random


class Card:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class AttackCard(Card):
    def __init__(self, name, description, damage,recul=0):
        super().__init__(name, description)
        self.damage = damage
        self.recul=recul

    def play(self, target,player):
        target.take_damage(self.damage)
        player.take_damage(self.recul)

class HealCard(Card):
    def __init__(self, name, description, healing,defense=0):
        self.defense=defense
        super().__init__(name, description)
        self.healing = healing

    def play(self, target,player):
        target=player
        target.defense_ch=self.defense
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


class Character:
    def __init__(self, name, max_hp):
        self.carte_possible=[]
        self.name = name
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.defense_ch=0
        self.deck = Deck()

    def take_damage(self, damage):
        damage-=self.defense_ch
        if damage<0:damage=0
        self.current_hp -= damage
        self.defense_ch=0
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
        self.cartes_possible_warrior=[AttackCard("Coup d'Épée", "Une attaque puissante avec une épée", damage=10)
                    ,AttackCard("lame lourde", "inflige de lourds dégats", damage=15,recul=2)
                     ,AttackCard("lame berserk", "coup surpuissant avec grand  recul", damage=25,recul=10)]
        super().__init__(name, max_hp=100)

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, max_hp=100)
        self.cartes_possible_mage=[AttackCard("boule de feu", "lance une puissante boule de feu", damage=10)
                    ,HealCard("bouclier sacré", "soigne et offre une modeste protection", healing=5,defense=10)
                     ,AttackCard("avadakedabra", "magie surpuissante avec grand recul", damage=30,recul=15)]

# class Thief(Character):
#     def __init__(self, name):
#         super().__init__(name, max_hp=150)

