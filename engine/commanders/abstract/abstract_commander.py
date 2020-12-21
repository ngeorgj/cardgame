#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.cards.abstract import Abstraction


class AbstractCommander(Abstraction):

    effect = []

    def action(self):
        """unique action"""