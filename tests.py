#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.game.cards.collection.expansion_sets.genesis.blue.mana.blue_mana import BlueMana
from engine.game.decks.black.base_blue_deck import base_genesis_blue_deck
from engine.game.environment.board import Board
from engine.game.environment.player import Player

nivaldo = Player()
ana = Player()

nivaldo.deck = base_genesis_blue_deck()
board = Board([nivaldo, ana])

print(nivaldo.deck.information())