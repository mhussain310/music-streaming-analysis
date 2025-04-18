import plotly.express as px
import streamlit as st

from config.db_config import CONNECTION_PARAM

# Streamlit custom component imports
from streamlit_app.components.add_expander import sql_query_result_expander
from streamlit_app.components.create_bar_chart import create_bar_chart
from streamlit_app.components.create_choropleth_map import create_choropleth_map
from streamlit_app.components.create_donut_chart import create_donut_chart
from streamlit_app.components.create_scatter_plot import create_scatter_plot
from streamlit_app.components.create_select_filter import create_select_filter
from streamlit_app.components.create_static_table import create_static_table
from streamlit_app.components.filter_df_with_select_box import filter_df_with_select_box

from streamlit_app.components.platform_popularity_by_country_chart import (
    plot_platform_popularity_by_country_chart,
)
from streamlit_app.styles.style import load_css

# Util imports
from utils.db_utils import get_db_connection
from utils.sql_utils import execute_sql_query

CSS_FILE_PATH_FROM_ROOT = "streamlit_app/styles/main.css"

# Page configuration
st.set_page_config(page_title="Global Music Streaming Trends & Listener Insights")

# Import custom css styles
load_css(CSS_FILE_PATH_FROM_ROOT)

# Open music DB connection
conn = get_db_connection(CONNECTION_PARAM)

st.title("Global Music Streaming Trends & Listener Insights")

# ----------------------------------------------------------------------------------

st.header("1. What was the most popular music platform?")
most_popular_platform = execute_sql_query("sql/most_popular_platform.sql", conn)
sql_query_result_expander(most_popular_platform)
create_bar_chart(
    most_popular_platform,
    title="Most Popular Streaming Platform by Percentage Users",
    x_label="Percentage Users",
    color_col="user_count_pct",
    use_continuous_color=True,
    custom_data_cols=["user_count"],
)

# ----------------------------------------------------------------------------------

st.header("2. How does genre preference vary by platform?")
genre_preference_by_platform = execute_sql_query(
    "sql/genre_preference_by_platform.sql", conn
)
sql_query_result_expander(genre_preference_by_platform)
config_q2 = {
    "num_selectbox": 1,
    "selectbox_filters": ["top_genre"],
    "selectbox_keys": ["genre_select_q2"],
    "selectbox_labels": ["Select a genre to compare across platforms"],
}
filtered_df_q2, selected_values_q2 = create_select_filter(
    genre_preference_by_platform, config_q2
)

create_bar_chart(
    filtered_df_q2,
    title=f"Platform Popularity for '{selected_values_q2['genre_select_q2']}' Genre",
    x_label="Percentage Users",
    custom_data_cols=["user_count"],
)

# ----------------------------------------------------------------------------------

st.header("3. How do listening times differ by platform?")
listening_times_by_platform = execute_sql_query(
    "sql/listening_times_by_platform.sql", conn
)
sql_query_result_expander(listening_times_by_platform)
config_q3 = {
    "num_selectbox": 1,
    "selectbox_filters": ["streaming_platform"],
    "selectbox_keys": ["platform_select_q3"],
    "selectbox_labels": ["Select a Streaming Platform"],
}
filtered_df_q3, selected_values_q3 = create_select_filter(
    listening_times_by_platform, config_q3
)
create_donut_chart(
    filtered_df_q3,
    title=f"Listening Time Distribution for {selected_values_q3['platform_select_q3']}",
    names="listening_time",
    custom_data_cols=["user_count"],
    hover_labels={
        "user_count": "Number of Users",
        "user_count_pct": "Percentage Users",
    },
)

# ----------------------------------------------------------------------------------

st.header("4. Which age group stream the most music?")
stream_by_age_group = execute_sql_query("sql/stream_by_age_group.sql", conn)
sql_query_result_expander(stream_by_age_group)
create_donut_chart(
    stream_by_age_group,
    title="User Distribution Across All Platforms by Age Group",
    custom_data_cols=["user_count"],
    hover_labels={
        "user_count": "Number of Users",
        "user_count_pct": "Percentage Users",
    },
)

# ----------------------------------------------------------------------------------

st.header("5. What age group spends the most time streaming?")
stream_duration_per_age_group = execute_sql_query(
    "sql/stream_duration_per_age_group.sql", conn
)
sql_query_result_expander(stream_duration_per_age_group)
create_bar_chart(
    stream_duration_per_age_group,
    title="Stream Duration per Age Group",
    is_percentage=False,
)

# ----------------------------------------------------------------------------------

st.header("6. What is the most popular genre per age group?")
most_popular_genre_per_age_group = execute_sql_query(
    "sql/most_popular_genre_per_age_group.sql", conn
)
sql_query_result_expander(most_popular_genre_per_age_group)
create_static_table(
    most_popular_genre_per_age_group,
    column_headers=[
        "Age Group",
        "Top Genre",
        "Max Count",
        "Total Users per Age Group",
        "Percentage Users",
    ],
    percent_columns=["max_count_pct"],
    integer_columns=["max_count", "total_user_per_age_group"],
)

# ----------------------------------------------------------------------------------

st.header("7. What are the country-level differences in listening times?")
listening_times_by_country = execute_sql_query(
    "sql/listening_times_by_country.sql", conn
)
sql_query_result_expander(listening_times_by_country)

config_q7 = {
    "num_multiselect": 2,
    "multiselect_filters": ["country", "listening_time"],
    "multiselect_keys": ["country_select_q7", "listening_time_select_q7"],
    "multiselect_labels": ["Select Countries", "Select Listening Time"],
}
filtered_df_q7, selected_values_q7 = create_select_filter(
    listening_times_by_country, config_q7
)

create_bar_chart(
    filtered_df_q7,
    title="Listening Time Distribution by Country",
    orientation="v",
    barmode="group",
    color_col="listening_time",
    x_label="Country",
    y_label="Percentage of Users",
    showlegend=True,
    hover_labels={"listening_time": "Listening Time"},
)

# ----------------------------------------------------------------------------------

st.header("8. Are users from certain countries listening to more music per day?")
stream_duration_per_country = execute_sql_query(
    "sql/stream_duration_per_country.sql", conn
)
sql_query_result_expander(stream_duration_per_country)
create_choropleth_map(
    stream_duration_per_country,
    title="Average Minutes Streamed Per Day by Country<br><sub><i>Countries in white indicate no available data</i></sub>",
    color="avg_mins_streamed_per_day",
    color_sequence=px.colors.sequential.Viridis[::-1],
    hover_labels={"avg_mins_streamed_per_day": "Avg Mins/Day"},
)

# ----------------------------------------------------------------------------------

st.header("9. Do users from particular countries prefer certain genres?")
genre_preference_by_country = execute_sql_query(
    "sql/genre_preference_by_country.sql", conn
)
sql_query_result_expander(genre_preference_by_country)
config_q9 = {
    "num_selectbox": 1,
    "selectbox_filters": ["top_genre"],
    "selectbox_keys": ["genre_select_q9"],
    "selectbox_labels": ["Select a genre to compare across countries"],
    "num_multiselect": 1,
    "multiselect_filters": ["country"],
    "multiselect_keys": ["country_select_q9"],
    "multiselect_labels": ["Select Countries"],
}
filtered_df_q9, selected_values_q9 = create_select_filter(
    genre_preference_by_country, config_q9
)
create_bar_chart(
    filtered_df_q9,
    title=f"Preference of {selected_values_q9['genre_select_q9']} Music Across Countries",
    orientation="v",
    x_axis="country",
    y_axis="user_count_pct",
    y_label="Percentage of Users",
    hover_labels={
        "top_genre": "Genre",
        "user_count_pct": "Percentage of Users",
        "user_count": "Number of Users",
    },
    custom_data_cols=["user_count", "top_genre"],
)

# ----------------------------------------------------------------------------------

st.header("10. What are the most popular streaming platforms across the globe?")
platform_popularity_by_country = execute_sql_query(
    "sql/platform_popularity_by_country.sql", conn
)
sql_query_result_expander(platform_popularity_by_country)
config_q10 = {
    "num_selectbox": 1,
    "selectbox_filters": ["streaming_platform"],
    "selectbox_keys": ["platform_select_q10"],
    "selectbox_labels": ["Select Streaming Platform"],
    "num_multiselect": 1,
    "multiselect_filters": ["platform_rank"],
    "multiselect_keys": ["rank_select_q10"],
    "multiselect_labels": ["Select Platform Rank(s)"],
    "multiselect_defaults": [1.0],
}
filtered_df_q10, selected_values_q10 = create_select_filter(
    platform_popularity_by_country, config_q10
)
plot_platform_popularity_by_country_chart(
    filtered_df_q10,
    selected_values_q10["platform_select_q10"],
    selected_values_q10["rank_select_q10"],
)

# ----------------------------------------------------------------------------------

st.header(
    "11. What is the average duration of streams per day for each streaming platform?"
)
stream_duration_per_platform = execute_sql_query(
    "sql/stream_duration_per_platform.sql", conn
)
sql_query_result_expander(stream_duration_per_platform)
create_bar_chart(
    stream_duration_per_platform,
    title="Average Minutes Streamed Per Day by Platform",
    is_percentage=False,
)

# ----------------------------------------------------------------------------------

st.header("12. Which genres are most associated with high repeat rate?")
repeat_rate_per_genre = execute_sql_query("sql/repeat_rate_per_genre.sql", conn)
sql_query_result_expander(repeat_rate_per_genre)
create_bar_chart(
    repeat_rate_per_genre,
    title="Average Repeat Rate per Genre",
    x_label="Average Repeat Rate (%)",
    y_label="Genre",
)

# ----------------------------------------------------------------------------------

st.header("13. Which age groups are most associated with high repeat rate?")
repeat_rate_per_age_group = execute_sql_query("sql/repeat_rate_per_age_group.sql", conn)
sql_query_result_expander(repeat_rate_per_age_group)
filtered_df_q13, selected_genre_q13 = filter_df_with_select_box(
    repeat_rate_per_age_group,
    column_filter="top_genre",
    filter_label="Select a Genre",
    keyname="select_box_query_13",
)
create_bar_chart(
    filtered_df_q13,
    title=f"Average Repeat Rate per Age Group for {selected_genre_q13} Music",
    x_axis="avg_repeat_rate_per_age_group",
    y_axis="age_group",
    x_label="Average Repeat Rate (%)",
    y_label="Age Group",
)

# ----------------------------------------------------------------------------------

st.header("14. What is the age distribution of users across platforms?")
age_dist_per_platform = execute_sql_query("sql/age_dist_per_platform.sql", conn)
sql_query_result_expander(age_dist_per_platform)
config_q14 = {
    "num_multiselect": 2,
    "multiselect_filters": ["streaming_platform", "age_group"],
    "multiselect_keys": ["platform_select_q14", "age_group_select_q14"],
    "multiselect_labels": ["Select Streaming Platform", "Select Age Group"],
}
filtered_df_q14, selected_values_q14 = create_select_filter(
    age_dist_per_platform, config_q14
)

create_bar_chart(
    filtered_df_q14,
    title="Age Distribution of Users Across Streaming Platforms",
    orientation="v",
    barmode="group",
    color_col="age_group",
    x_label="Streaming Platform",
    y_label="Percentage of Users",
    showlegend=True,
    custom_data_cols=["user_count"],
    hover_labels={"age_group": "Age Group", "user_count": "Number of Users"},
)

# ----------------------------------------------------------------------------------

st.header("15. What is the distribution of users across platforms in terms of country?")
country_dist_per_platform = execute_sql_query("sql/country_dist_per_platform.sql", conn)
sql_query_result_expander(country_dist_per_platform)
st.write(
    "This can be visualised through the chart in Q10. Select a streaming platform along with all ranks to get the distribution of users of a streaming platform across countries."
)

# ----------------------------------------------------------------------------------

st.header(
    "16. What is the distribution of users across platforms in terms of subscription type?"
)
sub_type_dist_per_platform = execute_sql_query(
    "sql/sub_type_dist_per_platform.sql", conn
)
sql_query_result_expander(sub_type_dist_per_platform)
create_bar_chart(
    sub_type_dist_per_platform,
    title="User Count by Subscription Type and Streaming Platform",
    orientation="v",
    barmode="group",
    color_col="subscription_type",
    x_label="Streaming Platform",
    y_label="Percentage of Users",
    showlegend=True,
    custom_data_cols=["user_count"],
    hover_labels={
        "subscription_type": "Subscription Type",
        "user_count": "Number of Users",
    },
)

# ----------------------------------------------------------------------------------

st.header("17. What are the most common subscription type for different age groups?")
sub_type_per_age_group = execute_sql_query("sql/sub_type_per_age_group.sql", conn)
sql_query_result_expander(sub_type_per_age_group)
create_bar_chart(
    sub_type_per_age_group,
    title="User Count by Subscription Type and Age Group",
    orientation="v",
    barmode="group",
    color_col="subscription_type",
    x_label="Age Group",
    y_label="Percentage of Users",
    showlegend=True,
    custom_data_cols=["user_count"],
    hover_labels={
        "subscription_type": "Subscription Type",
        "user_count": "Number of Users",
    },
)

# ----------------------------------------------------------------------------------

st.header("18. Do users listen more at specific times of the day?")
stream_duration_per_lis_time = execute_sql_query(
    "sql/stream_duration_per_lis_time.sql", conn
)
sql_query_result_expander(stream_duration_per_lis_time)
create_static_table(
    stream_duration_per_lis_time, float_columns=["avg_mins_streamed_per_day"]
)

# ----------------------------------------------------------------------------------

st.header(
    "19. Are users who prefer certain genres streaming more overall than those who listen to others?"
)
stream_duration_per_genre = execute_sql_query("sql/stream_duration_per_genre.sql", conn)
sql_query_result_expander(stream_duration_per_genre)
create_bar_chart(
    stream_duration_per_genre,
    title="Average Minutes Streamed per Day for Different Genres",
    orientation="v",
    x_label="Genre",
    is_percentage=False,
    color_col="avg_mins_streamed_per_day",
    use_continuous_color=True,
)

# ----------------------------------------------------------------------------------

st.header("20. Are certain artists more popular on specific platforms?")
artist_per_platform = execute_sql_query("sql/artist_per_platform.sql", conn)
sql_query_result_expander(artist_per_platform)
config_q20 = {
    "num_selectbox": 1,
    "selectbox_filters": ["most_played_artist"],
    "selectbox_keys": ["artist_select_q20"],
    "selectbox_labels": ["Select an artist to compare across platforms"],
}
filtered_df_q20, selected_values_q20 = create_select_filter(
    artist_per_platform, config_q20
)
create_bar_chart(
    filtered_df_q20,
    title=f"Distribution of Users Across Streaming Platforms Whose Most Played Artist Is {selected_values_q20['artist_select_q20']}",
    orientation="v",
    x_axis="streaming_platform",
    x_label="Streaming Platform",
    y_label="Percentage of Users",
    custom_data_cols=["most_played_artist", "user_count"],
    hover_labels={"most_played_artist": "Artist", "user_count": "Number of Users"},
)
# ----------------------------------------------------------------------------------

st.header("21. Do premium subscribers like more songs than free-tier users?")
likes_per_sub_type = execute_sql_query("sql/likes_per_sub_type.sql", conn)
sql_query_result_expander(likes_per_sub_type)
create_static_table(likes_per_sub_type, integer_columns=["total_songs_liked"])

# ----------------------------------------------------------------------------------

st.header(
    "22. Is there a difference in the listening time based on a user's subscription type?"
)
listening_times_per_sub_type = execute_sql_query(
    "sql/listening_times_per_sub_type.sql", conn
)
sql_query_result_expander(listening_times_per_sub_type)
create_bar_chart(
    listening_times_per_sub_type,
    title="Listening Times Based on Subscription Type",
    orientation="v",
    barmode="group",
    x_axis="listening_time",
    x_label="Listening Time",
    y_label="Percentage of Users",
    color_col="subscription_type",
    showlegend=True,
    custom_data_cols=["subscription_type", "user_count"],
    hover_labels={
        "subscription_type": "Subscription Type",
        "user_count": "Number of Users",
    },
)

# ----------------------------------------------------------------------------------

st.header(
    "23. Do users who engage more with Discover Weekly tend to repeat songs less or more?"
)
repeat_rate_per_discovery = execute_sql_query("sql/repeat_rate_per_discovery.sql", conn)
sql_query_result_expander(repeat_rate_per_discovery)
create_scatter_plot(
    repeat_rate_per_discovery,
    title="Discover Weekly Engagement vs Repeat Song Rate",
    x_label="Discover Weekly Engagement (%)",
    y_label="Repeat Song Rate (%)",
)

# ----------------------------------------------------------------------------------

st.header(
    "24. Are users who engage more with Discover Weekly more likely to like songs?"
)
likes_per_discovery = execute_sql_query("sql/likes_per_discovery.sql", conn)
sql_query_result_expander(likes_per_discovery)
create_scatter_plot(
    likes_per_discovery,
    title="Discover Weekly Engagement vs Number of Songs Liked",
    x_label="Discover Weekly Engagement (%)",
    y_label="Number of Songs Liked",
)

# ----------------------------------------------------------------------------------

# Close DB connection
conn.close()
