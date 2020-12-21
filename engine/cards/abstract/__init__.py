#
# // Repositories
#    github@ngeorgj
# 

# imports
from abc import ABC

from engine.environment.constants import Constants
from engine.environment.log import Log


class Abstraction(ABC, Log, Constants):
    """ Base Abstraction Parent Class"""

    name = ""
    description = ""

