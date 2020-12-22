#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.game.environment import MANA
from engine.game.environment.deck import Deck


class Player:

    name = ''
    deck: Deck = []

    hand = []
    battlefield = []

    attackers = []
    defenders = []

    graveyard = []
    mana_pool = 0
    is_playing = False

    active_effects = []
    active_curses = []

    hp = 20
    armor = 0

    def check_active_curses(self):
        # TODO: Implement game phase triggers
        for effect in self.active_curses:
            effect.activate(self)

    def check_active_effects(self):
        # TODO: Implement game phase triggers
        for effect in self.active_effects:
            effect.activate(self)

    def draw_card(self):
        top_deck_card = self.deck.cards[-1]
        self.deck.cards.remove(top_deck_card)
        self.hand.append(top_deck_card)

    def untap_all_mana(self):
        for card in self.battlefield:
            if card.card_type == MANA:
                card.untap()

    def tap_all_mana(self):
        for card in self.battlefield:
            if card.card_type == MANA:
                card.tap()

    def attrib_ownership_to_deck(self):
        for card in self.deck.cards:
            card.owner = self

    def turn(self, table):
        pass
