#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.game.abstract.card.abstract_creature import AbstractCreature
from engine.game.abstract.card.card_color import BlackCard
from engine.game.abstract.card.properties import FLYING
from engine.game.cards.collection.effects.common.add_stats import AddDamageAndThoughnessMarkersOnSummon
from engine.game.cards.collection.expansion_sets.genesis.expansion_class import Genesis


class BlackArchangel(Genesis, BlackCard, AbstractCreature):

    name = 'Black Archangel'

    description = 'An undead black angel with dark wings.'
    explanation = 'When Black Archangel enters the battlefield he gains one +1/+1 marker.'
    flavor_text = '"The darkness sometimes can prevail..." - unknown'

    race = 'Undead'
    adjective = 'Archangel'

    properties = [FLYING]

    cost = 4
    damage = 2
    toughness = 3

    @property
    def effects(self):
        return [AddDamageAndThoughnessMarkersOnSummon(self, 1, 1)]
