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
    cost = 0

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

        if not self.player_have_mana(player):
            return print("You don't have enough mana to cast spell.")

        else:  # If player has enough mana to cast the card.
            self.pay_mana_cost(player)
            print(f'\n[{player.name}] casts [{self.name}].\n\n  Card Description:\n  {self.description}\n')

            if self.effect.activate_on_cast:
                self.effect.trigger(player)

            player.hand.remove(self)
            player.battlefield.append(self)

            if self.effect.activate_on_battlefield:
                self.effect.trigger(player)

            return 100

    def tap(self):
        self.is_tapped = True

    def untap(self):
        self.is_tapped = False

    def send_to_graveyard(self, player):
        player.deck.remove(self)
        player.graveyard.append(self)

    def pay_mana_cost(self, card_owner):
        card_owner.mana_pool -= self.cost

    def player_have_mana(self, player):
        if player.mana_pool >= self.cost:
            return True
        return False

    def complete_cost(self):
        return f'{self.cost} {self.color}'

    def __repr__(self):
        return f'{self.name}'
