#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.game.abstract.effect.abstract_effect import AbstractEffect


class AddDamageAndThoughnessMarkersOnSummon(AbstractEffect):

    name = 'Strenght from Beyond'
    description = 'Adds one +1/+1 marker to the creature.'

    activate_on_summon = True

    def __init__(self, target, damage, thoughness):
        self.target = target
        self.damage = damage
        self.thoughness = thoughness

    def activate(self):
        self.target.damage += self.damage
        self.target.toughness += self.thoughness
