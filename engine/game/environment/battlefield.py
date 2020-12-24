#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.game.environment import CREATURE


class Battlefield:

    battlefield = []

    def creatures(self):
        return [c for c in self.battlefield if c.card_type == CREATURE]
