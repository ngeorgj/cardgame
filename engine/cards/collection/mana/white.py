#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.cards.abstract.card.abstract_mana import AbstractManaCard
from engine.cards.abstract.effect.abstract_mana import AbstractManaEffect


class WhiteMana(AbstractManaCard):

    color = 'White'
    effect = AbstractManaEffect()

