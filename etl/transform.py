import pandas as pd


def transform_data(data: pd.DataFrame) -> pd.DataFrame:
    # Rename columns to match the SQL table
    data.columns = [
        "user_id",
        "age",
        "country",
        "streaming_platform",
        "top_genre",
        "minutes_streamed_per_day",
        "number_of_songs_liked",
        "most_played_artist",
        "subscription_type",
        "listening_time",
        "discover_weekly_engagement_pct",
        "repeat_song_rate_pct",
    ]

    return data
