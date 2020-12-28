#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.game.abstract.card.abstract_creature import AbstractCreature
from engine.game.abstract.card.card_color import WhiteCard
from engine.game.cards.collection.expansion_sets.genesis.expansion_class import Genesis
from engine.game.environment import CREATURE


class ArcaneTaurus(Genesis, WhiteCard, AbstractCreature):
    name = 'Arcane Taurus'
    card_type = CREATURE
    
    description = 'Blessed taurus.'
    explanation = ""

    flavor_text = '"It comes right at you, he smells fear." - Peasant'

    race = 'Taurus'
    adjective = ''

    properties = []

    cost = 2
    damage = 2
    toughness = 3

