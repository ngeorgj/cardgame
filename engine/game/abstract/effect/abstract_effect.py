#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.game.abstract.abstraction import Abstraction
from engine.game.abstract.effect import EFFECTS


class AbstractEffect(Abstraction):
    """
    Abstraction of Card Effect.

    on new instances:
        > Add function 'activate' and expose the effect.

    the activate() function will be used in trigger() function.
    """
    effect_type: str = EFFECTS['OVERWRITE']

    effect = 0
    is_recurrent = False

    turns = 0
    max_turns = 0

    activate_on_cast = False
    activate_on_summon = False
    activate_on_beginning_phase = False
    activate_on_pre_combat_phase = False
    activate_on_combat_phase = False
    activate_on_attack = False
    activate_on_defense = False
    activate_on_post_combat_phase = False
    activate_on_death = False
    activate_on_graveyard = False
    activate_on_life_gain = False
    activate_on_life_loss = False
    activate_on_friendly_creature_enters_the_battlefield = False
    activate_on_enemy_creature_enters_the_battlefield = False
    activate_on_animal_enters_battlefield = False
    activate_on_demon_enters_battlefield = False

    target = ''   # player/enemy or creature

    triggered = False

    def trigger(self):
        self.activate()

    def __repr__(self):
        return self.name
