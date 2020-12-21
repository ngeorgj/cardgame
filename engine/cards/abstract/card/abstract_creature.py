#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.cards.abstract.card.abstract_card import AbstractCard


class AbstractCreature(AbstractCard):

    damage = 0
    thoughness = 0

    race = False
    adjective = False

    card_type = 'Creature'

    properties = []
    markers = []

    @property
    def subtitle(self):
        return f"{self.card_type} - {self.race} {self.adjective}"

    @property
    def stats(self):
        return f"{self.damage}/{self.thoughness}"

