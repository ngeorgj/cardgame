#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.game.abstract import AbstractManaCard
from engine.game.abstract import WhiteCard
from engine.game.cards import Genesis


class WhiteMana(Genesis, WhiteCard, AbstractManaCard):
    """"""
    explanation = 'This card adds 1 white mana to your mana pool when tapped.'
    flavor_text = '"The sky is calling... Should I answer?" - White Mage'

