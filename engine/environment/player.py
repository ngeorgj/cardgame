#
# // Repositories
#    github@ngeorgj
# 

# imports


class Player:

    name = ''
    deck = []

    @property
    def deck_size(self):
        return len(self.deck)

    hand = []
    battlefield = []
    graveyard = []
    mana_pool = 0

    active_effects = []
    active_curses = []

    commander = []

    def check_active_curses(self):
        for effect in self.active_curses:
            effect.activate(self)

    def check_active_effects(self):
        for effect in self.active_effects:
            effect.activate(self)
