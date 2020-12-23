#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.game.commanders.abstract.abstract_commander import AbstractCommander
import random


class Deck:

    name = 'Deck Name::Overwrite'
    cards = []

    commander: AbstractCommander = []

    def add_card(self, card):
        self.cards.append(card)

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
        cost = sum([card.cost for card in self.cards])
        return cost / self.deck_size

    def separate_by_cost(self):
        dct = {}
        counter = 0
        for card in self.cards:
            dct[f'{card.cost}'] = []

        for card in self.cards:
            dct[f"{card.cost}"].append(card)

            counter += 1

        return dct
