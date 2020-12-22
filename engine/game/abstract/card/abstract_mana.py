#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.game.environment import MANA
from engine.game.abstract.card.abstract_card import AbstractCard
from engine.game.abstract.effect.mana_effect import ManaEffect


class AbstractManaCard(AbstractCard):

    card_type = MANA

    @property
    def name(self):
        return f'{self.color} Mana'

    @property
    def description(self):
        effect = self.effects
        return f'{effect[0].description}'

    @property
    def effects(self):
        return [ManaEffect()]

    @property
    def information(self):
        return f"[{self.name}]{f'[0]':>{55-len(self.name)}}\n" \
               f"[E] {self.explanation}\n" \
               f"[F] {self.flavor_text}\n"
