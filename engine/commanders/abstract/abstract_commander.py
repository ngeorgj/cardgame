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

    def __repr__(self):
        return f'commander: {self.name}'