#
# // Repositories
#    github@ngeorgj
# 

# GAME INFORMATION
from engine.cards import all_cards
from engine.commanders import all_commanders
from engine.environment import WHITE, BLACK, BLUE

NAME: str = 'JAGUAR, THE GATHERING'

COLORS: set = {
    {WHITE: {'Commanders': [comm for comm in all_commanders if comm.color == WHITE]},
             'Cards':      [card for card in all_cards if card.color == WHITE]},

    {BLACK: {'Commanders': [comm for comm in all_commanders if comm.color == BLACK],
             'Cards':      [card for card in all_cards if card.color == BLACK]}},

    {BLUE: {'Commanders': [comm for comm in all_commanders if comm.color == BLUE],
            'Cards':      [card for card in all_cards if card.color == BLUE]}}}

PROPERTIES: dict = {
    'flying': 'creatures with flying cannot be blocked by creatures without flying'
}
