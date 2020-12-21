#
# // Repositories
#    github@ngeorgj
# 

# imports
import random


class Deck:

    name = ''
    cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)

    def shuffle(self):
        random.shuffle(self.cards)

    @property
    def deck_size(self):
        return len(self.cards)

    @property
    def avg_cost(self):
        cost = sum([card.cost for card in self.cards])
        return cost / self.deck_size