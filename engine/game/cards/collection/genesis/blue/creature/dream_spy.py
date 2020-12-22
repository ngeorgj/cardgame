#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.game.abstract import AbstractCreature
from engine.game.abstract import BlueCard
from engine.game.abstract.card.properties import FLYING
from engine.game.cards import Genesis


class DreamSpy(Genesis, BlueCard, AbstractCreature):

    name = 'Dream Spy'

    description = 'She likes to see what people are dreaming'
    explanation = ''
    flavor_text = '"I could sense her breathing inside my dream!" - unknown'

    race = 'Nymph'
    adjective = 'Spy'

    properties = [FLYING]

    cost = 1
    damage = 1
    toughness = 1
