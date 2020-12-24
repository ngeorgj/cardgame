#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.game.abstract.card.abstract_creature import AbstractCreature
from engine.game.abstract.card.card_color import BlackCard
from engine.game.abstract.effect.abstract_effect import AbstractEffect
from engine.game.cards.collection.expansion_sets.genesis.expansion_class import Genesis


class UndeadHydra(Genesis, BlackCard, AbstractCreature):
    name = 'Undead Hydra'

    description = 'A big mutant serpent with 3 heads.'
    explanation = 'This Hydra only dies if the damage is fatal. Else, the damage taken is converted in +1/+1 counters.'
    flavor_text = '"Not even the gods could handle this beast..." - Peasant'

    race = 'Hydra'
    adjective = 'Mutant Serpent'

    properties = []

    cost = 4
    damage = 3
    toughness = 3

    @property
    def effects(self):

        class AddMarkersEqualsToDamage(AbstractEffect):

            name = "Hydra's surprise!"

            activate_on_life_loss = True

            def __init__(self, target):
                self.effect = target.last_damage_taken
                self.target = target

            def activate(self, target: AbstractCreature):
                if target.last_damage_taken >= target.toughness:
                    target.send_to_graveyard_from_battlefield()
                else:
                    target.damage += self.effect
                    target.toughness += self.effect

        return [AddMarkersEqualsToDamage(self)]
