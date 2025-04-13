import pandas as pd
import streamlit as st

from config.db_config import CONNECTION_PARAM
from utils.db_utils import get_db_connection
from utils.sql_utils import execute_sql_query

# Open music DB connection
conn = get_db_connection(CONNECTION_PARAM)

st.title("Global Music Streaming Trends & Listener Insights")

st.header("1. What was the most popular music platform?")
most_popular_platform = execute_sql_query("sql/most_popular_platform.sql", conn)
st.write(most_popular_platform)

st.header("2. How does genre preference vary by platform?")
genre_preference_by_platform = execute_sql_query(
    "sql/genre_preference_by_platform.sql", conn
)
st.write(genre_preference_by_platform)

st.header("3. How do listening times differ by platform?")
listening_times_by_platform = execute_sql_query(
    "sql/listening_times_by_platform.sql", conn
)
st.write(listening_times_by_platform)

st.header("4. Which age group stream the most music?")
stream_by_age_group = execute_sql_query("sql/stream_by_age_group.sql", conn)
st.write(stream_by_age_group)

st.header("5. What age group spends the most time streaming?")
stream_duration_per_age_group = execute_sql_query(
    "sql/stream_duration_per_age_group.sql", conn
)
st.write(stream_duration_per_age_group)

st.header("6. What is the most popular genre per age group?")
most_popular_genre_per_age_group = execute_sql_query(
    "sql/most_popular_genre_per_age_group.sql", conn
)
st.write(most_popular_genre_per_age_group)

st.header("7. What are the country-level differences in listening times?")
listening_times_by_country = execute_sql_query(
    "sql/listening_times_by_country.sql", conn
)
st.write(listening_times_by_country)

st.header("8. Are users from certain countries listening to more music per day?")
stream_duration_per_country = execute_sql_query(
    "sql/stream_duration_per_country.sql", conn
)
st.write(stream_duration_per_country)

st.header("9. Do users from particular countries prefer certain genres?")
genre_preference_by_country = execute_sql_query(
    "sql/genre_preference_by_country.sql", conn
)
st.write(genre_preference_by_country)

st.header("10. What are the most popular streaming platforms across the globe?")
platform_popularity_by_country = execute_sql_query(
    "sql/platform_popularity_by_country.sql", conn
)
st.write(platform_popularity_by_country)

st.header(
    "11. What is the average duration of streams per day for each streaming platform?"
)
stream_duration_per_platform = execute_sql_query(
    "sql/stream_duration_per_platform.sql", conn
)
st.write(stream_duration_per_platform)

st.header("12. Which genres are most associated with high repeat rate?")
repeat_rate_per_genre = execute_sql_query("sql/repeat_rate_per_genre.sql", conn)
st.write(repeat_rate_per_genre)

st.header("13. Which age groups are most associated with high repeat rate?")
repeat_rate_per_age_group = execute_sql_query("sql/repeat_rate_per_age_group.sql", conn)
st.write(repeat_rate_per_age_group)

st.header("14. What is the age distribution of users across platforms?")
age_dist_per_platform = execute_sql_query("sql/age_dist_per_platform.sql", conn)
st.write(age_dist_per_platform)

st.header("15. What is the distribution of users across platforms in terms of country?")
country_dist_per_platform = execute_sql_query("sql/country_dist_per_platform.sql", conn)
st.write(country_dist_per_platform)

st.header(
    "16. What is the distribution of users across platforms in terms of subscription type?"
)
sub_type_dist_per_platform = execute_sql_query(
    "sql/sub_type_dist_per_platform.sql", conn
)
st.write(sub_type_dist_per_platform)

st.header("17. What are the most common subscription type for different age groups?")
sub_type_per_age_group = execute_sql_query("sql/sub_type_per_age_group.sql", conn)
st.write(sub_type_per_age_group)

st.header("18. Do users listen more at specific times of the day?")
stream_duration_per_lis_time = execute_sql_query(
    "sql/stream_duration_per_lis_time.sql", conn
)
st.write(stream_duration_per_lis_time)

st.header(
    "19. Are users who prefer certain genres streaming more overall than those who listen to others?"
)
stream_duration_per_genre = execute_sql_query("sql/stream_duration_per_genre.sql", conn)
st.write(stream_duration_per_genre)

st.header("20. Are certain artists more popular on specific platforms?")
artist_per_platform = execute_sql_query("sql/artist_per_platform.sql", conn)
st.write(artist_per_platform)

st.header("21. Do premium subscribers like more songs than free-tier users?")
likes_per_sub_type = execute_sql_query("sql/likes_per_sub_type.sql", conn)
st.write(likes_per_sub_type)

st.header(
    "22. Is there a difference in the listening time based on a user's subscription type?"
)
listening_times_per_sub_type = execute_sql_query(
    "sql/listening_times_per_sub_type.sql", conn
)
st.write(listening_times_per_sub_type)

st.header(
    "23. Do users who engage more with Discover Weekly tend to repeat songs less or more?"
)
st.write("Chart will be created to identify this trend.")

st.header(
    "24. Are users who engage more with Discover Weekly more likely to like songs?"
)
st.write("Chart will be created to identify this trend.")

# Close DB connection
conn.close()
