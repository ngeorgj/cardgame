#
# // Repositories
#    github@ngeorgj
# 

# imports
from abc import ABC
from engine.game.environment.log import Log


class Abstraction(ABC, Log):
    """ Base Abstraction Parent Class"""

    name = ""
    description = ""
    explanation = ''
    flavor_text = ''

