import pandas as pd

from utils.file_utils import get_absolute_path


def import_sql_query(file_path):
    try:
        absolute_file_path = get_absolute_path(file_path)
        with open(absolute_file_path, "r") as file:
            imported_query = file.read().replace("\n", " ").strip()
            return imported_query
    except FileNotFoundError as e:
        print(f"Failed to import query: {absolute_file_path} not found")


def execute_sql_query(file_path, conn):
    query = import_sql_query(file_path)
    query_result = pd.read_sql(query, conn)

    return query_result
