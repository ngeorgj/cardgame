#
# // Repositories
#    github@ngeorgj
# 

# imports
import random
from engine.game.abstract.card.abstract_creature import AbstractCreature
from engine.game.abstract.effect.abstract_effect import AbstractEffect


class KillRandomEnemyCreature(AbstractEffect):
    """
    An activator must be selected.

    activate_on_summon, etc.
    """

    def __init__(self, enemy_battlefield):
        self.enemy_battlefield = enemy_battlefield

    def activate(self):
        creature: AbstractCreature = random.choice(self.enemy_battlefield)
        print(f"Random Creature: {creature.name} sent to {creature.owner}'s graveyard.")
        creature.send_to_graveyard_from_battlefield()

