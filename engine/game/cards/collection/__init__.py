#
# // Repositories
#    github@ngeorgj
# 

# imports


# Compiled
from engine.game.cards.collection.expansion_sets.genesis import genesis_cards


def all_cards():
    card_list = []

    expansions = [
        genesis_cards,
        # Add more Expansion Sets here.
    ]

    for expansion in expansions:
        for color in expansion:
            card_list.extend(color)

    return card_list
