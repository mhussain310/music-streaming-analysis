import plotly.express as px
import streamlit as st


def create_donut_chart(
    df,
    title,
    names="",
    values="",
    is_percentage=True,
    custom_data_cols=None,
    color_sequence=None,
    hover_labels=None,
):
    names = df.columns[0] if names == "" else names
    values = df.columns[-1] if values == "" else values

    # Create chart
    fig = px.pie(
        df,
        names=f"{names}",
        values=f"{values}",
        hole=0.5,
        color_discrete_sequence=color_sequence or px.colors.qualitative.Pastel,
        custom_data=df[custom_data_cols] if custom_data_cols else None,
    )

    # Format text template
    text_fmt = (
        "%{label}<br>%{value:.2f}%" if is_percentage else "%{label}<br>%{percent:.2f}"
    )

    # Label formatting
    name_label = (
        hover_labels.get(names, names.replace("_", " ").title())
        if hover_labels
        else names.replace("_", " ").title()
    )
    value_label = (
        hover_labels.get(values, values.replace("_", " ").title())
        if hover_labels
        else values.replace("_", " ").title()
    )

    # Hover template construction
    hover_template_parts = [
        f"{name_label}: <b>%{{label}}</b>",
        f"{value_label}: <b>%{{value:.2f}}{'%' if is_percentage else ''}</b>",
    ]

    if custom_data_cols:
        for i, col in enumerate(custom_data_cols):
            pretty = (
                hover_labels.get(col, col.replace("_", " ").title())
                if hover_labels
                else col.replace("_", " ").title()
            )
            hover_template_parts.append(f"<b>{pretty}:</b> %{{customdata[{i}]}}")

    hover_template = "<br>".join(hover_template_parts)

    fig.update_traces(
        texttemplate=text_fmt,
        textposition="outside",
        hovertemplate=hover_template,
    )

    fig.update_layout(
        margin=dict(l=140, r=40, t=100, b=80),
        uniformtext_minsize=12,
        uniformtext_mode="hide",
        autosize=True,
        title=dict(x=0.5, xanchor="center", text=f"{title}"),
    )

    # Display the chart
    st.plotly_chart(fig, use_container_width=True)
