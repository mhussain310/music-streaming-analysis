import sqlite3


def get_db_connection(connection_params):
    connection = sqlite3.connect(connection_params)
    return connection
