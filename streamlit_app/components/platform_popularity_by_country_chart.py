import plotly.express as px
import streamlit as st

from streamlit_app.components.create_choropleth_map import create_choropleth_map
from utils.streamlit_utils import get_ordinal


def plot_platform_popularity_by_country_chart(df, selected_platform, selected_ranks):
    # Country Count Summary and Ordinal Ranks for the Title
    num_countries = df["country"].nunique()
    ordinal_ranks = [get_ordinal(int(r)) for r in selected_ranks]
    title_ranks = ", ".join(ordinal_ranks)

    create_choropleth_map(
        df,
        title=f"Countries Where {selected_platform} is Ranked {title_ranks}<br><sub><i>{selected_platform} is ranked {title_ranks} in <b>{num_countries}</b> countries.</i></sub>",
        color="user_count_pct",
        z_label="Percentage Users",
        color_sequence=px.colors.sequential.Viridis[::-1],
        hover_labels={"user_count": "Users"},
        custom_data_cols=["user_count", "platform_rank"],
        is_percentage=True,
    )

    # Tooltip note
    st.markdown(
        f"<div class='foot-note'>"
        f"Note: Countries not highlighted indicate that <b>{selected_platform}</b> was not ranked "
        f"{title_ranks} in those regions. If all platform ranks are selected and countries are still not highlighted, this means there was no available data for those countries."
        f"</div>",
        unsafe_allow_html=True,
    )
