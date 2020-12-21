#
# // Repositories
#    github@ngeorgj
# 

# imports
from abc import ABC
from engine.environment.log import Log


class Abstraction(ABC, Log):
    """ Base Abstraction Parent Class"""

    name = ""
    description = ""

