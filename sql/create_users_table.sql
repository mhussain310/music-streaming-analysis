CREATE TABLE IF NOT EXISTS users (
    user_id TEXT PRIMARY KEY,
    age INTEGER,
    country TEXT,
    streaming_platform TEXT,
    top_genre TEXT,
    minutes_streamed_per_day INTEGER,
    number_of_songs_liked INTEGER,
    most_played_artist TEXT,
    subscription_type TEXT,
    listening_time TEXT,
    discover_weekly_engagement_pct REAL,
    repeat_song_rate_pct REAL
);