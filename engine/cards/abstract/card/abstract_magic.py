#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.cards.abstract.card.abstract_card import AbstractCard
from engine.cards.abstract.effect.abstract_effect import AbstractEffect


class AbstractMagic(AbstractCard):

    card_type = 'Magic'

    effect: AbstractEffect = []

