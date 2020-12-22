#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.game.abstract import AbstractCreature
from engine.game.abstract.effect import AbstractEffect
from engine.game.abstract import WhiteCard
from engine.game.cards import Genesis


class CerineiaDoe(Genesis, WhiteCard, AbstractCreature):
    name = 'Cerineia Doe'
    description = 'A very fast doe.'
    explanation = 'When Cerineia Doe enters the battlefield, put\n' \
                  ' an +1/+1 marker in all the friendly creatures'

    flavor_text = '"Are you skilled enough to capture her?" - Euristeu'

    race = 'Doe'
    adjective = 'Runner'

    properties = []

    cost = 5
    damage = 4
    toughness = 6

    @property
    def effects(self):
        class AddOneOneMarkersToAllFriendlyCreatures(AbstractEffect):

            def __init__(self, target):
                self.target = target

            name = "Cerineia's Blessing"

            effect_type = 'Status'
            description = 'Adds one +1/+1 to all friendly creatures in the battlefield.'

            activate_on_summon = True

            def activate(self):
                for creature in self.target.battlefield:
                    creature.damage += 1
                    creature.toughness += 1

        return [AddOneOneMarkersToAllFriendlyCreatures(self.owner)]
