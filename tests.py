#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.game.cards.collection import all_cards

for card in all_cards():
    print(card.name)