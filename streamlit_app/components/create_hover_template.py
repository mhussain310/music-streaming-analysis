def create_hover_template(
    map_type,
    orientation="",
    x_label="",
    y_label="",
    location_label="",
    z_label="",
    hover_labels=None,
    custom_data_cols=None,
    is_percentage=True,
):
    # Hover template construction
    hover_template_parts = []

    if map_type == "choropleth":
        hover_template_parts.append(f"{location_label}: <b>%{{location}}</b>")
        hover_template_parts.append(
            f"{z_label}: <b>%{{z:.2f}}{'%' if is_percentage else ''}</b>"
        )
    else:
        if orientation == "v":
            hover_template_parts.append(f"{x_label}: <b>%{{x}}</b>")
            hover_template_parts.append(
                f"{y_label}: <b>%{{y:.2f}}{'%' if is_percentage else ''}</b>"
            )
        else:
            hover_template_parts.append(f"{y_label}: <b>%{{y}}</b>")
            hover_template_parts.append(
                f"{x_label}: <b>%{{x:.2f}}{'%' if is_percentage else ''}</b>"
            )

    if custom_data_cols:
        for i, col in enumerate(custom_data_cols):
            pretty = (
                hover_labels.get(col, col.replace("_", " ").title())
                if hover_labels
                else col.replace("_", " ").title()
            )
            hover_template_parts.append(f"{pretty}: <b>%{{customdata[{i}]}}</b>")

    hover_template = "<br>".join(hover_template_parts) + "<extra></extra>"
    return hover_template
