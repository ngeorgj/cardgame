#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.game.commanders.abstract.abstract_commander import AbstractCommander
import random

from engine.game.environment import MANA


class Deck:

    name = 'Deck Name::Overwrite'
    cards = []

    commander: AbstractCommander = []

    def add_card(self, card):
        card = card()
        self.cards.append(card)

    def add_cards(self, card_list: list):
        for card in card_list:
            self.add_card(card)

    def remove_card(self, card):
        self.cards.remove(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def attrib_ownership_to_deck(self, owner):
        for card in self.cards:
            card.owner = owner

    @property
    def deck_size(self):
        return len(self.cards)

    @property
    def avg_cost(self):
        list_of_cards = [card.cost for card in self.cards if card.card_type != MANA]
        cost = sum(list_of_cards)
        deck_size = len(list_of_cards)
        return cost / deck_size

    def separate_by_cost(self):
        dct = {}
        counter = 0
        for card in self.cards:
            dct[f'{card.cost}'] = []

        for card in self.cards:
            dct[f"{card.cost}"].append(card)
            counter += 1

        return dct

    @property
    def information(self):
        return f"Name:           {self.name} - {self.deck_size} cards.\n" \
               f"Color:          {self.cards[0].color}\n" \
               f"Avg. Cost:      {self.avg_cost} Mana\n" \
               f"Card List:      {[card.name for card in self.cards if card.card_type != MANA]}"

    def card_list(self):
        dct = {}
        for card in self.cards:
            dct[card.name] = len([c for c in self.cards if c.name == card.name])

        print('Card List')
        return ' \n'.join([f"{item[0]} {item[1]:>{20-len(item[0])}}" for item in dct.items()])