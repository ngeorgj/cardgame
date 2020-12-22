#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.game.abstract import AbstractCreature
from engine.game.abstract import WhiteCard
from engine.game.abstract.card.properties import FLYING
from engine.game.abstract.effect import HealingEffect
from engine.game.cards import Genesis


class Archangel(Genesis, WhiteCard, AbstractCreature):

    name = 'Archangel'

    description = "Angel that provides protection"
    explanation = 'When Archangel enters the battlefield, her\n summoner gains 1 point of life.'
    flavor_text = '"You can almost feel the breeze of his wings..." - devotee'

    race = 'Angel'
    adjective = ''

    properties = [FLYING]

    cost = 4
    damage = 2
    toughness = 3

    @property
    def effects(self):

        class OwnerGain1HP(HealingEffect):

            activate_on_summon = True

            def __init__(self, target):
                self.target = target

        return [OwnerGain1HP(self.owner)]


