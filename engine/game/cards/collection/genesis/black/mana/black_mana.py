#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.game.abstract.card.abstract_mana import AbstractManaCard
from engine.game.abstract.card.card_color import BlackCard
from engine.game.cards.collection.genesis.expansion_class import Genesis


class BlackMana(Genesis, BlackCard, AbstractManaCard):
    """"""
    explanation = 'This card adds 1 black mana to your mana pool when tapped.'
    flavor_text = '"The void is calling... Should I answer?" - Black Mage'
