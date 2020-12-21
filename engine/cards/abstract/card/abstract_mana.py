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

    @property
    def description(self):
        return f'Adds {self.effect.effect} {self.color} {self.card_type} to your mana pool.'
