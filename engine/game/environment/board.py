#
# // Repositories
#    github@ngeorgj
# 

# imports
import random

from engine.errors import CustomError
from engine.game.environment.phases import Phases


class Board(Phases):

    now_playing = ''

    triggers = []

    def __init__(self, players: list):
        if len(players) not in [2, 4]:
            CustomError.not_enough_players()
        self.players = players
        for player in players:
            player.board = self

    @property
    def winner(self):
        still_playing = [player for player in self.players if player.hp > 0]
        if len(still_playing) == 1:
            return still_playing[0]
        return False

    def pre_game(self):
        for player in self.players:
            player.deck.shuffle()
            print(f"`{player.name}'s deck was shuffled.")
            start_player = random.randint(0, len(self.players) - 1)
            starting_player = self.players[start_player]
            self.now_playing = starting_player
            starting_player.is_playing = True

    def main(self):
        while not self.winner:
            self.now_playing.turn(self)

