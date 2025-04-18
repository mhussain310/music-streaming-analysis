import plotly.express as px


def create_color_scheme(use_continuous_color, color_sequence):
    color_args = {}
    if use_continuous_color:
        color_args["color_continuous_scale"] = color_sequence or [
            "#4a90e2",
            "#1f77b4",
            "#0b3c5d",
        ]
    else:
        color_args["color_discrete_sequence"] = (
            color_sequence or px.colors.qualitative.Set2
        )

    return color_args
