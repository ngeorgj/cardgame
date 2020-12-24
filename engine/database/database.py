#
# // Repositories
#    github@ngeorgj
# 

# imports
from engine.game.cards.collection import all_cards
from engine.game.commanders import all_commanders
import sqlite3

"""
How to use this file.

    To create recreate all the tables based on coded data:

        - Set variable 'execute_all' to True.
        
        - Check the variables with the following prefixes:
            > drop
            > create
            > populate
            
            And change them according to your needs.
    
    The file will grab all the functions and execute them.
    
"""

# Variables
game_db = 'game'
user_db = 'users'
location = './files/'

execute_all = True

# CardsTable
drop_cards_table = True
create_cards_table = True
populate_cards_table = True

# CommandersTable
drop_comms_table = True
create_comms_table = True
populate_comms_table = True

# UsersTable
drop_users_table = True
create_users_table = True
populate_users_table = True


# Shared Functions
def commit_and_close(conn):
    """
    Grabs a connection. \n
    Commits changes. \n
    Closes the connection.

    :param conn: sqlite connection
    :return: None
    """
    conn.commit()
    conn.close()


def sql_insertion(conn, tablename, dictionary: dict, silent=True):
    """
    SQL Insertion function.
    
        This function grabs a connection and inserts data from dict to
        the designed table

    :param conn: sqlite connection
    :param tablename: str
    :param dictionary:  dict
    :param silent: bool
    :return: None
    """
    try:
        query = f"INSERT INTO {tablename}({','.join(dictionary.keys())}) " \
                f"VALUES({','.join('?' * len(dictionary.keys()))})", \
                [tuple([item[1] for item in dictionary.items()])]

        conn.executemany(query[0], query[1])

        if not silent:
            print(f'[success] data inserted on {tablename}.')

    except:
        print(f'[error] on inserting data on {tablename}.')


# Cards
def cards():
    """
    Cards Function

    Database: game.db
    Tablename: cards

    Uses 'all_cards' list from cards/__init__.

    Iterates trough all the cards adding them to the database.
    """
    db_name = game_db
    tablename = 'cards'

    cards_table_sql = f"""\
        CREATE TABLE IF NOT EXISTS {tablename} (
    
            id           integer        PRIMARY KEY AUTOINCREMENT,
            name         text                     UNIQUE NOT NULL,
            description  text                            NOT NULL,
            explanation  text                            NOT NULL,
            cost         text                            NOT NULL,
            color        text                            NOT NULL,
            expansion    text                            NOT NULL,
            year         int                             NOT NULL
    
        )"""

    cards_db = location + f'{db_name}.db'
    cards_connection = sqlite3.connect(cards_db)
    cards_cursor = cards_connection.cursor()

    if drop_cards_table:
        cards_cursor.execute(f'DROP TABLE IF EXISTS {tablename};')

    if create_cards_table:
        cards_cursor.execute(cards_table_sql)

    def create_all_cards():
        for card in all_cards():
            card = card()
            data = dict(name=card.name,
                        description=card.description,
                        explanation=card.explanation,
                        cost=card.cost,
                        color=card.color,
                        expansion=card.expansion,
                        year=card.year)

            sql_insertion(cards_connection, tablename, data)

        commit_and_close(cards_connection)

    if populate_cards_table:
        create_all_cards()

    return cards_cursor


# Commanders
def commanders():
    """
    Commanders Function

    Database: game.db
    Tablename: commanders

    Uses 'all_commanders' list from commanders/__init__.

    Iterates trough all the commanders adding them to the database.
    """
    db_name = game_db
    tablename = 'commanders'

    comms_table_query = f"""\
        CREATE TABLE IF NOT EXISTS {tablename} (
    
            id           integer        PRIMARY KEY AUTOINCREMENT,
            name         text       UNIQUE NOT NULL,
            description  text              NOT NULL,
            color        text              NOT NULL
    
        )"""
    commanders_db = location + f'{db_name}.db'
    commanders_connection = sqlite3.connect(commanders_db)
    commanders_cursor = commanders_connection.cursor()

    if drop_comms_table:
        commanders_cursor.execute(f'DROP TABLE IF EXISTS {tablename};')

    if create_comms_table:
        commanders_cursor.execute(comms_table_query)

    def create_all_commanders():
        for comm in all_commanders:
            comm = comm()
            data = dict(name=comm.name,
                        description=comm.description,
                        color=comm.color)

            sql_insertion(commanders_connection, tablename, data)

        commit_and_close(commanders_connection)

    if populate_comms_table:
        create_all_commanders()

    return commanders_cursor


# Users
def users():
    """
    Users Function

    Database: users.db
    Tablename: users

    Handles users.
    """
    db_name = user_db
    tablename = 'users'

    users_table_query = f"""\
        CREATE TABLE IF NOT EXISTS {tablename} (

            id           integer        PRIMARY KEY AUTOINCREMENT,
            name         text       UNIQUE NOT NULL,
            nickname     text              NOT NULL,
            password     text              NOT NULL,
            email        text              NOT NULL,
            roles        text              NOT NULL

        )"""
    users_db = location + f'{db_name}.db'
    users_connection = sqlite3.connect(users_db)
    users_cursor = users_connection.cursor()

    if drop_users_table:
        users_cursor.execute(f'DROP TABLE IF EXISTS {tablename};')

    if create_users_table:
        users_cursor.execute(users_table_query)

    def create_registers():
        # Create Admin
        data = dict(name='admin',
                    nickname='admin',
                    password='admin1',
                    email='ngj.netrunner@gmail.com',
                    roles='admin')

        sql_insertion(users_connection, tablename, data)

        # Create Player
        data = dict(name='PlayerName',
                    nickname='P4WN',
                    password='user_passcode',
                    email='someemail@gmail.com',
                    roles='player')

        sql_insertion(users_connection, tablename, data)

        commit_and_close(users_connection)

    if populate_users_table:
        create_registers()

    return users_cursor


functions = [
    users,
    cards,
    commanders
]

if execute_all:
    for func in functions:
        func()
