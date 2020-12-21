#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.cards.collection.mana.white import WhiteMana
from engine.environment.player import Player

mana_branco = WhiteMana()
player = Player()
player.name = "Ana Vitória"
player.hand.append(mana_branco)

mana_branco.cast(player)
