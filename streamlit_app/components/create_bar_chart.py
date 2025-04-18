import plotly.express as px
import streamlit as st

from streamlit_app.components.create_color_scheme import create_color_scheme
from streamlit_app.components.create_hover_template import create_hover_template


def create_bar_chart(
    df,
    title,
    orientation="h",
    barmode=None,
    x_axis="",
    y_axis="",
    x_label="",
    y_label="",
    text_col="",
    color_col="",
    category_order="total ascending",
    is_percentage=True,
    use_continuous_color=False,
    color_sequence=None,
    custom_data_cols=None,
    hover_labels=None,
    showlegend=False,
):
    # Axis logic
    if orientation == "v":
        x_axis = df.columns[0] if x_axis == "" else x_axis
        y_axis = df.columns[-1] if y_axis == "" else y_axis
        text_col = text_col or y_axis
        color_col = color_col or x_axis
    else:
        x_axis = df.columns[-1] if x_axis == "" else x_axis
        y_axis = df.columns[0] if y_axis == "" else y_axis
        text_col = text_col or x_axis
        color_col = color_col or y_axis

    x_label = x_label or x_axis.replace("_", " ").title()
    y_label = y_label or y_axis.replace("_", " ").title()

    labels = {
        x_axis: x_label,
        y_axis: y_label,
    }

    # Allow additional hover labels
    if hover_labels:
        labels.update(hover_labels)

    # Choose color scheme
    color_args = create_color_scheme(use_continuous_color, color_sequence)

    fig = px.bar(
        df,
        x=f"{x_axis}",
        y=f"{y_axis}",
        orientation=f"{orientation}",
        barmode=barmode if barmode else "relative",
        text=text_col,
        color=color_col,
        labels=labels,
        custom_data=df[custom_data_cols] if custom_data_cols else None,
        **color_args,
    )

    # Format text template
    text_fmt = "%{text:.2f}%" if is_percentage else "%{text:.2f}"

    # Create hover template
    hover_template = create_hover_template(
        "bar",
        orientation=orientation,
        x_label=x_label,
        y_label=y_label,
        hover_labels=hover_labels,
        custom_data_cols=custom_data_cols,
        is_percentage=is_percentage,
    )

    fig.update_traces(
        texttemplate=text_fmt,
        textposition="outside",
        cliponaxis=False,
        hovertemplate=hover_template,
    )
    fig.update_layout(
        yaxis={} if orientation == "v" else dict(categoryorder=category_order),
        plot_bgcolor="white",
        margin=dict(l=60, r=40, t=60, b=40),
        showlegend=showlegend if showlegend else False,
        coloraxis_showscale=False,
        autosize=True,
        title=dict(x=0.5, xanchor="center", text=f"{title}"),
    )

    st.plotly_chart(fig, use_container_width=True)
