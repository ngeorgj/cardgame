#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.cards.abstract.card.abstract_mana import AbstractManaCard
from engine.cards.abstract.effect.abstract_mana import AbstractManaEffect
from engine.cards.collection.colors import WhiteCard


class WhiteMana(WhiteCard, AbstractManaCard):

    effect = AbstractManaEffect()
