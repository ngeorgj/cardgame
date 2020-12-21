#
# // Repositories
#    github@ngeorgj
#

# imports
from engine.cards.abstract import Abstraction
from engine.cards.abstract.effect.abstract_effect import AbstractEffect


class AbstractCard(Abstraction):
    """
    The abstract abstraction of a playable card.

    Contains basic information and effect: AbstractEffect

     > Parent Class Abstraction(ABC)

        - name
        - description

    """
    expansion: str = 'Genesis'
    card_type = ''
    color = ''

    effect: AbstractEffect = []

    is_tapped = False

    def cast(self, player):
        """
        Card Casting Flow

            1. Checks if the card trigger happens on cast.
            2. Remove the card from Player's hand.
            3. Put card on battlefield.
            4. Check if card trigger happens on battlefield.

        :param player:
        :return:
        """
        print(f'\n[{player.name}] casts [{self.name}].\n\n  Card Description:\n  {self.description}\n')
        if self.effect.activate_on_cast:
            self.effect.trigger(player)

        player.hand.remove(self)
        player.battlefield.append(self)

        if self.effect.activate_on_battlefield:
            self.effect.trigger(player)

    def tap(self):
        self.is_tapped = True

    def untap(self):
        self.is_tapped = False

    def send_to_graveyard(self, player):
        player.deck.remove(self)
        player.graveyard.append(self)
