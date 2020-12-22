#
# // Repositories
#    github@ngeorgj
# 

# imports

class EffectActivationHandler:

    def check_for_triggers_on_cast(self):
        for effect in self.effects:
            if effect.activate_on_cast:
                effect.trigger()
                if not effect.is_recurrent:
                    effect.triggered = True

    def check_for_triggers_on_battlefield(self):
        for effect in self.effects:
            if effect.activate_on_summon:
                effect.trigger()
                if not effect.is_recurrent:
                    effect.triggered = True

    def check_for_triggers_on_beginning_phase(self):
        for effect in self.effects:
            if effect.activate_on_beginning_phase:
                effect.trigger()
                if not effect.is_recurrent:
                    effect.triggered = True

    def check_for_triggers_on_pre_combat_phase(self):
        for effect in self.effects:
            if effect.activate_on_pre_combat_phase:
                effect.trigger()
                if not effect.is_recurrent:
                    effect.triggered = True

    def check_for_triggers_on_combat_phase(self):
        for effect in self.effects:
            if effect.activate_on_combat_phase:
                effect.trigger()
                if not effect.is_recurrent:
                    effect.triggered = True

    def check_for_triggers_on_attack(self):
        for effect in self.effects:
            if effect.activate_on_attack:
                effect.trigger()
                if not effect.is_recurrent:
                    effect.triggered = True

    def check_for_triggers_on_defense(self):
        for effect in self.effects:
            if effect.activate_on_defense:
                effect.trigger()
                if not effect.is_recurrent:
                    effect.triggered = True

    def check_for_triggers_on_post_combat_phase(self):
        for effect in self.effects:
            if effect.activate_on_post_combat_phase:
                effect.trigger()
                if not effect.is_recurrent:
                    effect.triggered = True

    def check_for_triggers_on_death(self):
        for effect in self.effects:
            if effect.activate_on_death:
                effect.trigger()
                if not effect.is_recurrent:
                    effect.triggered = True

    def check_for_triggers_on_graveyard(self):
        for effect in self.effects:
            if effect.activate_on_graveyard:
                effect.trigger()
                if not effect.is_recurrent:
                    effect.triggered = True

    def check_for_triggers_on_life_gain(self):
        for effect in self.effects:
            if effect.activate_on_life_gain:
                effect.trigger()
                if not effect.is_recurrent:
                    effect.triggered = True

    def check_for_triggers_on_life_loss(self):
        for effect in self.effects:
            if effect.activate_on_life_loss:
                effect.trigger()
                if not effect.is_recurrent:
                    effect.triggered = True
