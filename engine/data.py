#
# // Repositories
#    github@ngeorgj
# 

# GAME INFORMATION
from engine.game.abstract.card.properties import FLYING
from engine.game.cards.collection import all_cards
from engine.game.commanders import all_commanders
from engine.game.environment import WHITE, BLACK, BLUE

NAME: str = "CardGame"

COLORS = {
    {WHITE: {
        'Commanders': [comm for comm in all_commanders if comm.color == WHITE]},
        'Cards': [card for card in all_cards() if card.color == WHITE]},

    {BLACK: {
        'Commanders': [comm for comm in all_commanders if comm.color == BLACK],
        'Cards': [card for card in all_cards() if card.color == BLACK]}},

    {BLUE: {
        'Commanders': [comm for comm in all_commanders if comm.color == BLUE],
        'Cards': [card for card in all_cards() if card.color == BLUE]}}}

PROPERTIES: dict = {
    FLYING: 'creatures with flying cannot be blocked by creatures without flying'
}
