#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.cards.abstract.card.abstract_card import AbstractCard


class AbstractManaCard(AbstractCard):

    card_type = 'mana'

    @property
    def name(self):
        return f'{self.color} Mana'

    def function(self):
        pass