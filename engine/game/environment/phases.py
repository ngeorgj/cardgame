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
        self.state.phase = PHASE_BEGINNING
        player.draw_card()
        return self.state

    def pre_combat_phase(self, player):
        self.state.phase = PHASE_PRE_COMBAT
        player.choose_attackers()
        for attacker in player.attackers:
            attacker.tap()
        return self.state

    def combat_phase(self, player):
        self.state.phase = PHASE_COMBAT
        if len(player.attackers) != 0:
            for attacker in player.attackers:
                attacker.attack(attacker.target)
                attacker.target = ''

        return self.state

    def post_combat_phase(self, player):
        self.state.phase = PHASE_POST_COMBAT
        return self.state

    def ending_phase(self, player):
        self.state.phase = PHASE_ENDING
        return self.state

    def flow(self, player):
        self.beginning_phase(player)
        self.pre_combat_phase(player)
        self.combat_phase(player)
        self.post_combat_phase(player)
        self.ending_phase(player)