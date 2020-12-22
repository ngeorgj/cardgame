#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.game.abstract.card.abstract_mana import AbstractManaCard
from engine.game.abstract.card.card_color import BlueCard
from engine.game.cards.collection.expansion_sets.genesis.expansion_class import Genesis


class BlueMana(Genesis, BlueCard, AbstractManaCard):
    """"""
    explanation = 'This card adds 1 blue mana to your mana pool when tapped.'
    flavor_text = '"The Sea is calling... Should I answer?" - Blue Mage'
