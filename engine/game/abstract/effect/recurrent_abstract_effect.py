#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.game.abstract.effect.abstract_effect import AbstractEffect


class RecurrentAbstractEffect(AbstractEffect):

    effect_type = 'Recurrent'
    is_recurrent = True

    def trigger(self):
        self.activate()
