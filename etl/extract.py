import pandas as pd
from utils.file_utils import get_absolute_path

CSV_PATH = get_absolute_path("data/raw/music_trends.csv")


def extract_data() -> pd.DataFrame:
    try:
        # Extract CSV into pandas dataframe
        users_df = pd.read_csv(CSV_PATH, skiprows=1, header=None)
        return users_df
    except Exception as e:
        raise Exception(f"Failed to load CSV file: {CSV_PATH}")
