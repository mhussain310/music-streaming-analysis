def import_sql_query(filename):
    try:
        with open(filename, "r") as file:
            imported_query = file.read().replace("\n", " ").strip()
            return imported_query
    except FileNotFoundError as e:
        print(f"Failed to import query: {filename} not found")
