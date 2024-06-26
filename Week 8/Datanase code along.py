import sqlite3


class DBase:

    _conn = None
    _cursor = None




def __init_(self, db_name):
    self._db_name = db_name
    self.connect()

def connect(self):
    self._conn = sqlite3.connect(self._db_name)
    self._cursor = self._conn.cursor()


def excecute_script(self, sql_string):
    self._cursor.excecutescript(sql_string)


@property
def get_cursor(self):
    return self._cursor

@property
def get_connection(self):
    return self._conn
