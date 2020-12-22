#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.game.abstract.effect import EFFECTS
from engine.game.abstract.effect.abstract_effect import AbstractEffect


class HealingEffect(AbstractEffect):

    effect_type = EFFECTS['HEAL']
    effect = 1

    def activate(self):
        self.target.hp += self.effect
        self.message(f'{self.target.name} healed {self.effect} points of life.')
