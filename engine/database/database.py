#
# // Repositories
#    github@ngeorgj
# 

# imports
import sqlite3
from engine.cards import all_cards

# database files location
from engine.commanders import all_commanders

location = './files/'


# base function

def commit_and_close(conn):
    """Simplifies commits and closing."""
    conn.commit()
    conn.close()


# Cards
def cards(create_cards=False):
    tablename = 'cards'

    cards_creation_query = f"""\
        CREATE TABLE IF NOT EXISTS {tablename} (
    
            id           integer      PRIMARY KEY AUTOINCREMENT,
            name         text                   UNIQUE NOT NULL,
            description  text                          NOT NULL,
            color        text                          NOT NULL,
            cost         text                          NOT NULL
    
        )"""

    cards_db = location + f'{tablename}.db'
    cards_connection = sqlite3.connect(cards_db)
    cards_cursor = cards_connection.cursor()
    cards_cursor.execute(cards_creation_query)

    def create_all_cards():

        def sql(_id, name, description, color, cost):
            return f'INSERT INTO {tablename} VALUES ({_id}, "{name}", "{description}", "{color}", {cost})'

        counter = 1
        for card in all_cards:
            try:
                card = card()
                cards_cursor.execute(sql(counter, card.name, card.description, card.color, card.cost))
                counter += 1

            except:
                print(f'Error inserting {card.name} into SQLITE3.')

        commit_and_close(cards_connection)

    if create_cards:
        create_all_cards()

    return cards_cursor


# Commanders
def commanders(create_commanders=False):
    tablename = 'commanders'

    commanders_creation_query = f"""\
        CREATE TABLE IF NOT EXISTS {tablename} (
    
            id           integer      PRIMARY KEY,
            name         text     UNIQUE NOT NULL,
            description  text            NOT NULL,
            color        text            NOT NULL
    
        )"""
    commanders_db = location + 'commanders.db'
    commanders_connection = sqlite3.connect(commanders_db)
    commanders_cursor = commanders_connection.cursor()
    commanders_cursor.execute(commanders_creation_query)

    def create_all_commanders():

        def sql(_id, name, description, color):
            return f'INSERT INTO {tablename} VALUES ({_id}, "{name}", "{description}", "{color}")'

        counter = 1
        for comm in all_commanders:
            try:
                comm = comm()
                commanders_cursor.execute(sql(counter, comm.name, comm.description, comm.color))

            except:
                print(f'Error inserting {comm.name} into SQLITE db.')

        commit_and_close(commanders_connection)

    if create_commanders:
        create_all_commanders()

    return commanders_cursor


cards = cards(True)

commanders = commanders(True)
