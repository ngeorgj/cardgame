#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.game.abstract.card.abstract_creature import AbstractCreature
from engine.game.abstract.card.card_color import BlackCard
from engine.game.cards.collection.expansion_sets.genesis.expansion_class import Genesis


class DeathWalker(Genesis, BlackCard, AbstractCreature):
    name = 'Death Walker'

    description = 'The one who died and came back'
    explanation = ''
    flavor_text = '"To walk between the living... You must be strong.." - Death Walker'

    race = 'Zombie'
    adjective = ''

    properties = []

    cost = 1
    damage = 1
    toughness = 1


