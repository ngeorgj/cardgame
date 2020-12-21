#
# // Repositories
#    github@ngeorgj
# 

# imports
import random

from engine.errors import not_enough_players


class Board:

    def __init__(self, players: list):
        if len(players) not in [2, 4]:
            not_enough_players()
        self.players = players

    @property
    def winner(self):
        still_playing = [player for player in self.players if player.hp > 0]
        if len(still_playing) == 1:
            return still_playing[0]
        return False

    def start_game(self):
        for player in self.players:
            player.deck.shuffle()
            print(f"`{player.name}'s deck was shuffled.")

        start_player = random.randint(0, len(self.players) - 1)

    def play(self):
        pass

    def main(self):
        while not self.winner:
            self.play()
