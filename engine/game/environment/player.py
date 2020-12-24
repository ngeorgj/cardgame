#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.game.abstract.abstract_card_functions import AbstractCardFunctions
from engine.game.environment import MANA
from engine.game.environment.battlefield import Battlefield
from engine.game.environment.board import Board
from engine.game.environment.deck import Deck
from engine.game.environment.graveyard import Graveyard


class Player(Battlefield, Graveyard, AbstractCardFunctions):

    id = 0

    name = ''
    nickname = ''

    deck: Deck = []

    board: Board = []

    hand = []

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

    def turn(self, table):
        pass

    def actions(self):
        cards = self.hand
        cards_dict = {}
        counter = 1
        for card in cards:
            cards_dict[str(counter)] = card.name
            counter += 1
