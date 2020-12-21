#
# // Repositories
#    github@ngeorgj
# 

# imports
import sqlite3

location = './files/'

# Cards
cards_creation_query    = """\
    CREATE TABLE IF NOT EXISTS cards (

        id           integer      PRIMARY KEY,
        name         text     UNIQUE NOT NULL,
        description  text            NOT NULL,
        cost         text            NOT NULL

    )"""
cards_db                = location + 'cards.db'
cards_connection        = sqlite3.connect(cards_db)
cards_cursor            = cards_connection.cursor()

# Commanders
commands_creation_query = """\
    CREATE TABLE IF NOT EXISTS commanders (

        id           integer      PRIMARY KEY,
        name         text     UNIQUE NOT NULL,
        description  text            NOT NULL,

    )"""
commanders_db           = location + 'commanders.db'
commanders_connection   = sqlite3.connect(commanders_db)
commanders_cursor       = commanders_connection.cursor()

