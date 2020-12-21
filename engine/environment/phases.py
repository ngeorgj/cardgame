#
# // Repositories
#    github@ngeorgj
# 

# imports

# CONSTANTS
PHASE_BEGINNING = 'beginning-phase'
PHASE_PRE_COMBAT = 'pre-combat-phase'
PHASE_COMBAT = 'combat-phase'
PHASE_POST_COMBAT = 'post-combat-phase'
PHASE_ENDING = 'ending-phase'


class Phases:
    """
    Phases

        State holds the possibilities of each phase.

       > beginning_phase():
            player draws a card

            player can:
                summon creatures
                cast spells
                pass turn

       > pre_combat_phase():

            player can:
                summon creatures
                cast spells
                pass turn

       > combat_phase():

            player need to:
                if no creatures in field:
                    pass turn

                else:
                    pass turn or...
                    choose attackers.

       > post_combat_phase():

            player can:
                summon creatures
                cast spells

       > ending_phase():

            pass automatically.



    """
    class State:

        def __init__(self):
            self.summon = True
            self.cast_spells = True
            self.phase = PHASE_BEGINNING

    state = State()

    def beginning_phase(self, player):
        self.draw_card(player)
        self.can_cast_spells = True
        self.can_summon = True
        return self.can_summon, self.can_cast_spells


