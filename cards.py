from __future__ import annotations

class Card:
    pass

    def __init__(self, name: str,value: int):
        self._name = name
        self._value= value

    def __str__(self):
        return f"""{self._name} has {self._value} value"""
        
  
    def get_name(self):
        return self._name
    
    def get_value(self):
        return self._value


class attack_card(Card):
    def __str__(self):
        return f"""{self._name} has {self._value} attack value"""

class defense_card(Card):
    def __str__(self):
        return f"""{self._name} has {self._value} defense value"""
