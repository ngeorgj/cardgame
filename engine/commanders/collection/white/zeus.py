#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.commanders.abstract.abstract_commander import AbstractCommander
from engine.commanders.abstract.effect.recurrent_heal import RecurrentHealingEffect


class Zeus(AbstractCommander):

    name = 'Zeus'
    description = 'The King of the Olympo.'

    effect = RecurrentHealingEffect()

    @property
    def color(self):
        return self.WHITE

    @property
    def action_target(self):
        return self.PLAYER

    def action(self):
        pass