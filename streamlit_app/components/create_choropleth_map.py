import plotly.express as px
import streamlit as st
from streamlit_app.components.create_hover_template import create_hover_template
from streamlit_app.components.create_color_scheme import create_color_scheme


def create_choropleth_map(
    df,
    title,
    location_mode="country names",
    locations="country",
    location_label="",
    color="",
    z_label="",
    use_continuous_color=True,
    color_sequence=None,
    custom_data_cols=None,
    hover_labels=None,
    is_percentage=False,
):
    location_label = location_label or locations.replace("_", " ").title()
    z_label = z_label or color.replace("_", " ").title()

    labels = {
        locations: location_label,
        color: z_label,
    }

    # Allow additional hover labels
    if hover_labels:
        labels.update(hover_labels)

    # Choose color scheme
    color_args = create_color_scheme(use_continuous_color, color_sequence)

    fig = px.choropleth(
        df,
        locations=locations,
        locationmode=location_mode,
        color=color,
        labels=labels,
        custom_data=df[custom_data_cols] if custom_data_cols else None,
        **color_args
    )

    # Create hover template
    hover_template = create_hover_template(
        "choropleth",
        location_label=location_label,
        z_label=z_label,
        is_percentage=is_percentage,
        hover_labels=hover_labels,
        custom_data_cols=custom_data_cols,
    )

    fig.update_traces(
        hovertemplate=hover_template,
    )

    fig.update_layout(
        geo=dict(showframe=False, showcoastlines=True),
        margin=dict(l=40, r=40, t=60, b=40),
        autosize=True,
        title=dict(text=title, x=0.5, xanchor="center"),
    )

    st.plotly_chart(fig, use_container_width=True)
