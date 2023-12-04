from __future__ import annotations

from game import Warrior, Mage,Enemy, AttackCard,HealCard

import random

def choose_cards(player):
    # Cette fonction permet au joueur de choisir les cartes à jouer dans son deck
    print(f"\nC'est à {player.name} de jouer:")
    player_cards = player.deck.cards
    for i, card in enumerate(player_cards, start=1):
        if type(card)==AttackCard:
            print(f"{i}. {card.name} - {card.description} attack:{card.damage} recul: {card.recul} ")
        elif(type(card)==HealCard) :
            print(f"{i}. {card.name} - {card.description} heal:{card.healing} shield:{card.defense} ")

    chosen_cards_indices = input("Choisissez les cartes à jouer (séparées par des virgules) : ")
    chosen_cards_indices = [int(index) - 1 for index in chosen_cards_indices.split(",")]

    chosen_cards = [player_cards[index] for index in chosen_cards_indices]
    return chosen_cards

def main():
    # Créer le joueur
    player_choice = input("Choisissez votre classe (Warrior, Mage): ")
    if player_choice.lower() == "warrior":
        player = Warrior("Aragorn")
        player.carte_possible=player.cartes_possible_warrior
    elif player_choice.lower() == "mage":
        player = Mage("Gandalf")
        player.carte_possible=player.cartes_possible_mage
    # elif player_choice.lower() == "thief":
    #     player = Thief("Balkany")
    else:
        print("Classe non valide. Choisissez parmi Warrior, Mage")
        return

    # Ajouter des cartes au deck du joueur
    player.deck.add_card(random.choice(player.carte_possible))
    player.deck.add_card(random.choice(player.carte_possible))
    # Ajoutez d'autres cartes au besoin

    # Créer les ennemis
    enemies = [Enemy("Dragon", max_hp=50, attack=8 ), Enemy("Goblin", max_hp=30, attack=5), Enemy("Orc", max_hp=40, attack=13)]

    for enemy in enemies:
        print(f"\nVous entrez en combat contre {enemy.name}!")
        print(f"{enemy.name}: {enemy.current_hp}/{enemy.max_hp} HP")


        # Boucle de combat
        while player.is_alive() and enemy.is_alive():
            # Joueur choisit ses cartes
            chosen_cards = choose_cards(player)

            # Joueur joue ses cartes
            for card in chosen_cards:
                card.play(enemy,player)
                player.deck.remove_card(card)
            if enemy.is_alive()==False:
                pass
            else:
                player.take_damage(enemy.ennemy_attack)
                print(f"\n{enemy.name} attaque {player.name} avec {enemy.ennemy_attack} de dégâts.")
            player.deck.add_card(random.choice(player.carte_possible))

            print(f"\n{player.name}: {player.current_hp}/{player.max_hp} HP")
            print(f"{enemy.name}: {enemy.current_hp}/{enemy.max_hp} HP")
                
            

        # Fin du combat
        if player.is_alive():
            print(f"\nVous avez vaincu {enemy.name}!")
            player.deck.add_card(random.choice(player.carte_possible))
        else:
            print(f"\n{enemy.name} vous a vaincu. Game Over.")

if __name__ == "__main__":
    main()
