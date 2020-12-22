#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.game.commanders.abstract.abstract_commander import AbstractCommander
from engine.game.commanders import RecurrentHealingEffect
from engine.game.environment import WHITE


class Zeus(AbstractCommander):

    name = 'Zeus'
    description = 'The King of the Olympo.'

    effect = RecurrentHealingEffect()

    @property
    def color(self):
        return WHITE

    @property
    def action_target(self):
        return PLAYER

    def action(self):
        pass