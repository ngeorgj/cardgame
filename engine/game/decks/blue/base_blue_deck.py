#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.game.cards.collection.expansion_sets.genesis.blue.creature.dream_spy import DreamSpy
from engine.game.cards.collection.expansion_sets.genesis.blue.creature.sea_zealoth import SeaZealoth
from engine.game.cards.collection.expansion_sets.genesis.blue.mana.blue_mana import BlueMana
from engine.game.environment.deck import Deck


def base_genesis_blue_deck():
    base_blue_deck = Deck()
    base_blue_deck.name = 'Dream Burst::StarterDeck'
    base_blue_deck.add_cards([
        BlueMana, BlueMana, BlueMana, BlueMana, BlueMana, BlueMana, BlueMana,
        BlueMana, BlueMana, BlueMana, BlueMana, BlueMana, BlueMana, BlueMana,
        SeaZealoth, SeaZealoth, SeaZealoth, DreamSpy, DreamSpy
    ])
    return base_blue_deck
