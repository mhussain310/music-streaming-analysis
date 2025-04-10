import pandas as pd

from config.db_config import CONNECTION_PARAM
from utils.db_utils import get_db_connection
from utils.file_utils import get_absolute_path
from utils.sql_utils import import_sql_query


def load_data(data: pd.DataFrame) -> None:
    # Creates or Opens existing DB
    conn = get_db_connection(CONNECTION_PARAM)

    # Create users table in DB
    create_table(conn)

    # Load dataframe into users table in DB
    data.to_sql("users", conn, if_exists="replace", index=False)

    print("Successfully created or updated table!")

    # Close DB connection
    conn.close()


def create_table(conn):
    cursor = conn.cursor()

    QUERY_PATH = get_absolute_path("sql/create_users_table.sql")
    create_users_table_query = import_sql_query(QUERY_PATH)

    cursor.execute(create_users_table_query)
    conn.commit()


if __name__ == "__main__":
    load_data()
