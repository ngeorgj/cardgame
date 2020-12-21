#
# // Repositories
#    github@ngeorgj
#

"""
import sqlite3

# INTERFACE IDEA
class DatabaseTable:
    location = './files/'

    table_create_sql = ''

    _drop_table = False
    _create_table = False
    _populate_table = False

    def __init__(self, db_name, tablename, table_create_sql: str = None, iterable: list = None):
        self.tablename = tablename
        self.db = f'{self.location}{db_name}.db'
        self.connection = sqlite3.connect(self.db)
        self.cursor = self.connection.cursor()

        if table_create_sql:
            self._create_table = True
            self.create_table()

            if iterable:
                self._populate_table = True
                self.iterable = iterable
                self.populate()

    def insert(self, data: dict):
        dictionary = data
        silent = True

        try:
            query = f"INSERT INTO {self.tablename}({','.join(dictionary.keys())}) " \
                    f"VALUES({','.join('?' * len(dictionary.keys()))})", \
                    [tuple([item[1] for item in dictionary.items()])]

            self.cursor.executemany(query[0], query[1])

            if not silent:
                print(f'[success] data inserted on {self.tablename}.')

        except:
            print(f'[error] on inserting data on {self.tablename}.')

    def populate(self):
        for obj in self.iterable:
            self.insert(obj)

    def create_table(self):
        self.cursor.execute(self.table_create_sql)

    def drop_table(self):
        self.cursor.execute(f'DROP TABLE {self.tablename};')

"""


