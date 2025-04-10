import pandas as pd

from config.db_config import CONNECTION_PARAM
from utils.db_utils import get_db_connection

conn = get_db_connection(CONNECTION_PARAM)

query = "SELECT COUNT(*) FROM users"
# query = "SELECT age, COUNT(user_id) FROM users GROUP BY age ORDER BY 2 DESC"
result = pd.read_sql(query, conn)
print(result.head())

conn.close()
