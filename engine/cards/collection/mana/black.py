#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.cards.abstract.card.abstract_mana import AbstractManaCard
from engine.cards.abstract.effect.abstract_mana import AbstractManaEffect


class BlackMana(AbstractManaCard):

    name = 'Black Mana'
    color = 'White'

    effect = AbstractManaEffect()

    @property
    def description(self):
        return f'Adds {self.effect.effect} {self.card_type} to your mana pool.'