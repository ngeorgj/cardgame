#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.cards import WhiteMana, BlackArchangel
from engine.environment.deck import Deck

deck = Deck()
deck.add_card(WhiteMana())
deck.add_card(BlackArchangel())


print(deck.separate_by_cost())