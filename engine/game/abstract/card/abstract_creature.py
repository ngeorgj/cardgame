#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.game.environment import CREATURE
from engine.game.abstract.card.abstract_card import AbstractCard


class AbstractCreature(AbstractCard):

    damage = 0
    toughness = 0

    race = False
    adjective = False

    card_type = CREATURE

    properties = []
    markers = []

    last_damage_taken = 0

    def attack(self, target):

        has_defense = len(target.defenders) > 0

        if has_defense:
            defenders = target.defenders

            for creature in defenders:
                self.check_battle_results(creature)

        else:
            target.hp -= self.damage
            self.message(f'{self.name} deals {self.damage} to {target.name}.')

    @property
    def subtitle(self):
        return f"{self.card_type} - {self.race} {self.adjective}"

    @property
    def stats(self):
        return f"{self.damage}/{self.toughness}"

    def check_battle_results(self, enemy_creature):
        this_creature_dies = enemy_creature.damage >= self.toughness
        enemy_creature_dies = self.damage >= enemy_creature.toughness

        if this_creature_dies:
            self.message(f'{self.name} dies during combat against {enemy_creature.name}.')
            self.send_to_graveyard_from_battlefield()

            self.check_for_triggers_on_death()                                                    # TRIGGER?

        else:
            self.toughness -= enemy_creature.damage
            self.check_for_triggers_on_life_loss()                                                # TRIGGER?

            enemy_creature.toughness -= self.damage
            enemy_creature.check_for_triggers_on_life_loss()                                      # TRIGGER?

        if enemy_creature_dies:
            self.message(f'{enemy_creature.name} dies during combat against {self.name}.')

            enemy_creature.send_to_graveyard_from_battlefield()
            enemy_creature.check_for_triggers_on_death()                                          # TRIGGER?

        else:
            self.toughness -= enemy_creature.damage
            self.check_for_triggers_on_life_loss()                                                # TRIGGER?

            enemy_creature.toughness -= self.damage
            enemy_creature.check_for_triggers_on_life_loss()                                      # TRIGGER?

    @property
    def information(self):
        name = f'[{self.name}]'
        subtitle = f' {self.subtitle}'
        cost = f'{self.complete_cost}'
        stats = f'[{self.stats}]'
        properties = ''
        if len(self.properties) > 0:
            properties = f"{', '.join([prop.title() for prop in self.properties])}"
        expansion = f'{self.expansion[0]}{str(self.year)[-2:]}'

        data = f"""\
{name} {cost:>{63-len(name)-len(cost)}} 
{subtitle}
 {self.description}
 {properties}
 {self.explanation}
 {'-' * len(self.flavor_text)}
 {self.flavor_text}

 by {self.card_creator} {expansion}       {stats:>{45-len(self.card_creator)-len(self.stats)}}
        """
        return data

    def straight_info(self):
        return f"[{self.name} {self.stats}]"
