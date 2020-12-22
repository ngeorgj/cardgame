#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.game.environment import MANA
from engine.game.abstract.effect.abstract_effect import AbstractEffect


class ManaEffect(AbstractEffect):
    name = 'Mana Source'

    effect_type = MANA

    activate_on_beginning_phase = True
    activate_on_summon = True

    mana_to_add = 1

    @property
    def description(self):
        return f'Adds {self.mana_to_add} mana to your mana pool.'

    def activate(self):
        self.target.mana_pool += self.mana_to_add
