#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.game.abstract.card.abstract_mana import AbstractManaCard
from engine.game.abstract.card.card_color import WhiteCard
from engine.game.cards.collection.expansion_sets.genesis.expansion_class import Genesis


class WhiteMana(Genesis, WhiteCard, AbstractManaCard):
    """"""
    explanation = 'This card adds 1 white mana to your mana pool when tapped.'
    flavor_text = '"The sky is calling... Should I answer?" - White Mage'

