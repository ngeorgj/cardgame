#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.game.abstract.card.abstract_creature import AbstractCreature
from engine.game.abstract.card.card_color import WhiteCard
from engine.game.abstract.effect.abstract_effect import AbstractEffect
from engine.game.cards.collection.expansion_sets.genesis.expansion_class import Genesis
from engine.game.environment import LEGENDARY_CREATURE


class Leonidas(Genesis, WhiteCard, AbstractCreature):
    name = 'Leonidas, King of Sparta'
    card_type = LEGENDARY_CREATURE
    
    description = 'the king of the spartans and the leader of the legendary army'
    explanation = "When Leonidas enters the battlefield, your creatures gain +1/+1"

    flavor_text = '"Spartans, what is your profession? - AU!" - Leonidas'

    race = 'Human'
    adjective = 'Warrior'

    properties = []

    cost = 4
    damage = 4
    toughness = 4

    @property
    def effects(self):
        class AddOneOneMarkersToAllFriendlyCreatures(AbstractEffect):

            def __init__(self, target):
                self.target = target

            name = "The law of Sparta"

            effect_type = 'Status'
            description = 'Adds one +1/+1 to all friendly creatures in the battlefield.'

            activate_on_summon = True

            def activate(self):
                for creature in self.target.battlefield:
                    creature.damage += 1
                    creature.toughness += 1

        return [AddOneOneMarkersToAllFriendlyCreatures(self.owner)]
