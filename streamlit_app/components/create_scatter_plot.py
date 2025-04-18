import plotly.express as px
import streamlit as st

from streamlit_app.components.create_hover_template import create_hover_template


def create_scatter_plot(
    df,
    title,
    orientation="v",
    x_axis="",
    y_axis="",
    x_label="",
    y_label="",
    opacity=0.6,
    template="plotly_white",
    is_percentage=False,
    custom_data_cols=None,
    hover_labels=None,
):
    # Axis logic
    if orientation == "v":
        x_axis = df.columns[0] if x_axis == "" else x_axis
        y_axis = df.columns[-1] if y_axis == "" else y_axis
    else:
        x_axis = df.columns[-1] if x_axis == "" else x_axis
        y_axis = df.columns[0] if y_axis == "" else y_axis

    x_label = x_label or x_axis.replace("_", " ").title()
    y_label = y_label or y_axis.replace("_", " ").title()

    labels = {
        x_axis: x_label,
        y_axis: y_label,
    }

    # Allow additional hover labels
    if hover_labels:
        labels.update(hover_labels)

    fig = px.scatter(
        df,
        x=f"{x_axis}",
        y=f"{y_axis}",
        labels=labels,
        opacity=opacity,
        template=template,
        custom_data=df[custom_data_cols] if custom_data_cols else None,
    )

    hover_template = create_hover_template(
        "scatter",
        orientation=orientation,
        x_label=x_label,
        y_label=y_label,
        hover_labels=hover_labels,
        custom_data_cols=custom_data_cols,
        is_percentage=is_percentage,
    )

    fig.update_traces(hovertemplate=hover_template)

    fig.update_layout(
        title=dict(x=0.5, xanchor="center", text=f"{title}"),
        height=600,
        margin=dict(l=50, r=50, t=60, b=50),
    )

    st.plotly_chart(fig, use_container_width=True)
