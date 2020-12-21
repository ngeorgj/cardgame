#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.cards.abstract.card.abstract_creature import AbstractCreature
from engine.cards.collection.colors import BlackCard
from engine.cards.collection.properties import FLYING


class BlackArchangel(BlackCard, AbstractCreature):

    name = 'Black Archangel'
    description = 'He flies between the living and the dead..'

    cost = 4

    damage = 2
    thoughness = 3

    race = 'Undead'
    adjective = 'Archangel'

    properties = [FLYING]

