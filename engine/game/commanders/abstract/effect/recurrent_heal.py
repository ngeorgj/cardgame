#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.game.abstract.effect import AbstractEffect


class RecurrentHealingEffect(AbstractEffect):

    activate_on_beginning_phase = True
    effect = 1

    activate_every_turn = True

    @property
    def target(self):
        return self.PLAYER

    def activate(self, target_player):
        target_player.hp += self.effect

