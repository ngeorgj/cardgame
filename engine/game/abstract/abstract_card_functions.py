#
# // Repositories
#    github@ngeorgj
# 

# imports

class AbstractCardFunctions:

    def get_from_battlefield(self, name):
        for card in self.battlefield:
            if card.name == name:
                return card

    def get_from_graveyard(self, name):
        for card in self.graveyard:
            if card.name == name:
                return card