#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.game.abstract import AbstractCreature
from engine.game.abstract import BlueCard
from engine.game.cards import Genesis


class SeaZealoth(Genesis, BlueCard, AbstractCreature):

    name = 'Sea Zealoth'

    description = 'Half horse, half fish'
    explanation = ''
    flavor_text = '"You can see the waves being formed by him.." - unknown'

    race = 'Hippocampus'
    adjective = ''

    properties = []

    cost = 3
    damage = 3
    toughness = 3
