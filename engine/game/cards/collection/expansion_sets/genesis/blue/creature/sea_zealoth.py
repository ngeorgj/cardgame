#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.game.abstract.card.abstract_creature import AbstractCreature
from engine.game.abstract.card.card_color import BlueCard
from engine.game.cards.collection.expansion_sets.genesis.expansion_class import Genesis


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
