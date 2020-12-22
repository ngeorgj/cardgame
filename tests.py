#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.game.cards import all_cards

for card in all_cards():
    card = card()
    print(card.information)