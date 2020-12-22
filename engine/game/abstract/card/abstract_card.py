#
# // Repositories
#    github@ngeorgj
#

# imports
from engine.game.abstract.abstraction import Abstraction
from engine.game.abstract.effect.effect_activation_handler import EffectActivationHandler
from engine.game.environment.player import Player


class AbstractCard(Abstraction, EffectActivationHandler):
    """
    The abstract abstraction of a playable card.

    Contains basic information and effect: AbstractEffect

     > Parent Class Abstraction(ABC)

        - name
        - description

    """
    expansion: str = ''

    card_type = ''
    cost = 0

    owner: Player = ''
    effects: list = []

    is_tapped = False

    def cast(self):
        """
        Card Casting Flow

            1. Checks if the card trigger happens on cast.
            2. Remove the card from Player's hand.
            3. Put card on battlefield.
            4. Check if card trigger happens on battlefield.

        :param player:
        :return:
        """

        if not self.player_have_mana():
            return print("You don't have enough mana to cast spell.")

        else:
            # If player has enough mana to cast the card.
            self.pay_mana_cost()
            self.casting_text()
            self.check_for_triggers_on_cast()

            self.owner.hand.remove(self)
            self.owner.battlefield.append(self)

            self.check_for_triggers_on_battlefield()

    def tap(self):
        self.is_tapped = True

    def untap(self):
        self.is_tapped = False

    def send_to_graveyard_from_hand(self):
        self.owner.hand.remove(self)
        self.owner.graveyard.append(self)

    def send_to_graveyard_from_battlefield(self):
        self.owner.battlefield.remove(self)
        self.owner.graveyard.append(self)

    def pay_mana_cost(self):
        self.owner.mana_pool -= self.cost

    def player_have_mana(self):
        if self.owner.mana_pool >= self.cost:
            return True
        return False

    @property
    def complete_cost(self):
        return f'{self.cost} {self.color}'

    def casting_text(self):
        return f'{self.owner.name} Casts {self.name} | Cost {self.complete_cost}'


    def __repr__(self):
        return f'{self.name}'

