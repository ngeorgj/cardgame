#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.cards.abstract.effect import EFFECTS
from engine.cards.abstract.effect.abstract_effect import AbstractEffect


class AbstractDamageEffect(AbstractEffect):

    _fx_type = EFFECTS['DAMAGE']

    effect = 1

    def activate(self, target_player):
        target_player.life -= self.effect
        self.message(f'{self.name} deals {self.effect} points damage at')
