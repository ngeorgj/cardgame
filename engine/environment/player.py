#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.environment.deck import Deck


class Player:

    name = ''
    deck: Deck = []

    hand = []
    battlefield = []
    graveyard = []
    mana_pool = 0

    active_effects = []
    active_curses = []

    hp = 20
    armor = 0

    def check_active_curses(self, game_phase):
        # TODO: Implement game phase triggers
        for effect in self.active_curses:
            effect.activate(self)

    def check_active_effects(self, game_phase):
        # TODO: Implement game phase triggers
        for effect in self.active_effects:
            effect.activate(self)

    def draw_card(self):
        top_deck_card = self.deck.cards[-1]
        self.deck.cards.remove(top_deck_card)
        self.hand.append(top_deck_card)

