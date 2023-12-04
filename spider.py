from __future__ import annotations

from dice import Dice
from random import randint

class Monstre:
    
    def __init__(self, name: str, max_hp: int, attack: int, defense: int, attack_spe: int, bonus_spe: int, dice: Dice):
        self._name = name
        self._max_hp = max_hp
        self._current_hp = max_hp
        self._attack_value = attack
        self._defense_value = defense
        self._attack_value_spe = attack_spe
        self._bonus_spe = bonus_spe
        self._dice = dice
        self.attaque_spe_used = False

    def __str__(self):
        return f"""{self._name} entre dans l'arène avec :
    ■ attaque : {self._attack_value} 
    ■ défense : {self._defense_value}"""
    
    def choose_action(self, target: Monstre):
        pass

    def get_defense_value(self):
        return self._defense_value
        
    def get_name(self):
        return self._name
        
    def is_alive(self):
        return self._current_hp > 0       

    def show_healthbar(self):
        missing_hp = self._max_hp - self._current_hp
        healthbar = f"[{"♥" * self._current_hp}{"♡" * missing_hp}] {self._current_hp}/{self._max_hp}hp"
        print(healthbar)

    def regenerate(self):
        self._current_hp = self._max_hp

    def decrease_health(self, amount):
        self._current_hp -= amount
        if self._current_hp < 0:
            self._current_hp = 0
        self.show_healthbar()
        
    def compute_damages(self, target):
        return self._attack_value
        
    def attack(self, target: Monstre):
        if not self.is_alive():
            return
        damages = self.compute_damages(target)
        print(f"⚔️ {self._name} attaque {target.get_name()} avec {damages} dégâts (attaque: {self._attack_value})")
        target.defense(damages, self)
    
    def compute_defense(self, damages, attacker):
        return damages - self._defense_value
    
    def defense(self, damages, attacker: Monstre):
        wounds = self.compute_defense(damages, attacker)
        print(f"🛡️ {self._name} subit {wounds} blessures de {attacker.get_name()} (dégâts: {damages} - défense: {self._defense_value})")
        self.decrease_health(wounds)
        

class Spider(Monstre):

    def compute_damages(self, target):
        if not self.is_alive() or self.attaque_spe_used:
            return super().compute_damages(target)

        roll = self._dice.roll()

        if roll in [5, 6]:
            damages = self._attack_value_spe 
            print((f"⚔️ {self._name} lance un fil sur  {target.get_name()} et lui mets {damages} dégâts (attaque spéciale: {self._attack_value_spe})"))
            target.defense(damages, self)
            self.attaque_spe_used = True
            return damages
        else:
            return super().compute_damages(target)

    def compute_bonus(self, target):
        return self._bonus_spe
    
    def bonus_spe(self, target: Monstre):
        if self._current_hp < 5 :
            bonus = self.compute_bonus(target)
            print(f"⚔️ {self._name} mange ant-man et se soigne de {bonus} Hp ( la vie gagner et de  {self._bonus_spe} Hp)")
            target.decrease_health(-bonus)

    def choose_action(self, target: Monstre):
        if self.is_alive() and not self.attaque_spe_used:
            roll = self._dice.roll()
            if roll in [1, 2, 3, 4]:
                self.attack(target)
            else:
                self.bonus_spe(target)
                self.attaque_spe_used = True
    
class Chauve_souris(Monstre):

    def compute_damages(self, target: Monstre):
        if not self.is_alive() or self.attaque_spe_used:
            return super().compute_damages(target)

        roll = self._dice.roll()

        if roll in [5, 6]:
            damages = self._attack_value_spe 
            print((f"⚔️ {self._name} emet des ultrason a {target.get_name()} et lui inflige {damages} dégâts (attaque spéciale: {self._attack_value_spe})"))
            target.defense(damages, self)
            self.attaque_spe_used = True
            return damages
        else:
            return super().compute_damages(target)

    def compute_bonus(self, target):
        return self._bonus_spe
    
    def bonus_spe(self, target: Monstre):
        if self._current_hp < 10 :
            bonus = self.compute_bonus(target)
            print(f"⚔️ {self._name} invoque batman et la guerie de {bonus} hp (gagne {self._bonus_spe} points de vie)")
            target.decrease_health(-bonus)
    
    def choose_action(self, target: Monstre):
        if self.is_alive() and not self.attaque_spe_used:
            roll = self._dice.roll()
            if roll in [1, 2, 3, 4]:
                self.attack(target)
            else:
                self.bonus_spe(target)
                self.attaque_spe_used = True
                           
                
class Dragon(Monstre):

    def compute_damages(self, target: Monstre):
        if not self.is_alive() or self.attaque_spe_used:
            return super().compute_damages(target)

        roll = self._dice.roll()

        if roll in [5, 6]:
            damages = self._attack_value_spe 
            print((f"⚔️ {self._name} crache du feu sur {target.get_name()} est inflige {damages} dégâts (attaque spéciale: {self._attack_value_spe})"))
            target.defense(damages, self)
            self.attaque_spe_used = True
            return damages
        else:
            return super().compute_damages(target)

    def compute_bonus(self, target):
        return self._bonus_spe
    
    def bonus_spe(self, target: Monstre):
        if self._current_hp < 10 :
            bonus = self.compute_bonus(target)
            print(f"⚔️ {self._name} mange du feu et gagne un bonus de {bonus} (le feu soigne de {self._bonus_spe} points de vie)")
            target.decrease_health(-bonus)
            self.attaque_spe_used = True
    
    def choose_action(self, target: Monstre):
        if self.is_alive() and not self.attaque_spe_used:
            roll = self._dice.roll()
            if roll in [1, 2, 3, 4]:
                self.attack(target)
            else:
                self.bonus_spe(target)
                self.attaque_spe_used = True