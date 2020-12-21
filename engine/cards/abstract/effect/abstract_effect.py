#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.cards.abstract import Abstraction
from engine.cards.abstract.effect import EFFECTS, ACTIVATION_METHODS


class AbstractEffect(Abstraction):
    """
    Abstraction of Card Effect.

    on new instances:
        > Add function 'activate' and expose the effect.

    the activate() function will be used in trigger() function.
    """
    _fx_type: str = EFFECTS['OVERWRITE']
    _trigger: str = ACTIVATION_METHODS['OVERWRITE']

    effect = 0

    turns = 0
    max_turns = 0

    activate_every_turn = False
    activate_on_cast = False
    activate_on_battlefield = False
    activate_on_beginning_phase = False
    activate_on_pre_combat_phase = False
    activate_on_combat_phase = False
    activate_on_attack = False
    activate_on_defense = False
    activate_on_post_combat_phase = False
    activate_leaving_battlefield = False
    activate_on_graveyard = False

    target = ''   # player/enemy

    def trigger(self, target_player):
        self.activate(target_player)

    def effect_type(self):
        return EFFECTS[self._fx_type]
