#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.game.abstract.effect import EFFECTS
from engine.game.abstract.effect.abstract_effect import AbstractEffect


class DamageEffect(AbstractEffect):

    effect_type = EFFECTS['DAMAGE']

    effect = 1

    def activate(self, target_player):
        target_player.life -= self.effect
        self.message(f'{self.name} deals {self.effect} points damage at')
