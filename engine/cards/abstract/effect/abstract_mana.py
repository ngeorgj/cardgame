#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.cards.abstract.effect import EFFECTS
from engine.cards.abstract.effect.abstract_effect import AbstractEffect


class AbstractManaEffect(AbstractEffect):

    _fx_type = EFFECTS['MANA']

    activate_on_battlefield = True
    activate_on_beginning_phase = True
    activate_every_turn = True

    effect = 1

    def activate(self, target_player):
        print(f"Card {self.name} triggered.")
        target_player.mana_pool += self.effect
