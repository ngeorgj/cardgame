#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.cards.abstract.effect import EFFECTS
from engine.cards.abstract.effect.abstract_effect import AbstractEffect


class AbstractHealingEffect(AbstractEffect):

    _fx_type = EFFECTS['HEAL']

    effect = 1

    def activate(self):
        self.target.life += self.effect
        self.message(f'{self.target.name} healed {self.effect} points of hp.')
