#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.game.abstract import AbstractManaCard
from engine.game.abstract import BlueCard
from engine.game.cards import Genesis


class BlueMana(Genesis, BlueCard, AbstractManaCard):
    """"""
    explanation = 'This card adds 1 blue mana to your mana pool when tapped.'
    flavor_text = '"The Sea is calling... Should I answer?" - Blue Mage'
