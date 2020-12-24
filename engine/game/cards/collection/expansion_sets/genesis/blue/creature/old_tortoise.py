#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.game.abstract.card.abstract_creature import AbstractCreature
from engine.game.abstract.card.card_color import BlueCard
from engine.game.abstract.card.properties import FLYING
from engine.game.cards.collection.expansion_sets.genesis.expansion_class import Genesis


class OldTortoise(Genesis, BlueCard, AbstractCreature):

    name = 'Old Tortoise'

    description = 'This is a very old animal that swims across the world.'
    explanation = ''
    flavor_text = '"What is that?" - Sailor'

    race = 'Ancient Tortoise'
    adjective = ''

    properties = [FLYING]

    cost = 3
    damage = 1
    toughness = 4
