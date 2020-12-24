#
# // Repositories
#    github@ngeorgj
# 

# imports
#from engine.game.cards.collection.expansion_sets.genesis.black.creature.undead_hydra import UndeadHydra
#from engine.game.cards.collection.expansion_sets.genesis.white.creature.archangel import Archangel
from engine.game.decks.black.base_blue_deck import base_genesis_blue_deck
from engine.game.environment.player import Player

#user1 = Player()
#user1.deck = base_genesis_blue_deck()

#user2 = Player()
#user2.deck = base_genesis_blue_deck()

#user2.defenders.append(user2.battlefield.get)

player = Player()
player.deck = base_genesis_blue_deck()
print(player.deck.card_list())