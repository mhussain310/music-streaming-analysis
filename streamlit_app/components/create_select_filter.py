import streamlit as st


def create_select_filter(df, config: dict):
    # Get config values or default fallbacks
    num_selectbox = config.get("num_selectbox", 0)
    selectbox_filters = config.get("selectbox_filters", [])
    selectbox_keys = config.get("selectbox_keys", [])
    selectbox_labels = config.get("selectbox_labels", [])

    num_multiselect = config.get("num_multiselect", 0)
    multiselect_filters = config.get("multiselect_filters", [])
    multiselect_keys = config.get("multiselect_keys", [])
    multiselect_labels = config.get("multiselect_labels", [])
    multiselect_defaults = config.get("multiselect_defaults", [])

    filtered_df = df.copy()

    selected_values = {}

    # Create selectboxes
    for i in range(num_selectbox):
        column = selectbox_filters[i]
        key = selectbox_keys[i]
        label = selectbox_labels[i]

        options = sorted(filtered_df[column].dropna().unique())
        selected = st.selectbox(label, options, key=key)
        selected_values[key] = selected
        filtered_df = filtered_df[filtered_df[column] == selected]

    # Create multiselects
    for i in range(num_multiselect):
        column = multiselect_filters[i]
        key = multiselect_keys[i]
        label = multiselect_labels[i]
        default = multiselect_defaults[i] if i < len(multiselect_defaults) else None

        options = sorted(filtered_df[column].dropna().unique())
        default_list = options[:5] if len(options) >= 5 else options
        default_option = default if default else default_list
        selected = st.multiselect(label, options, default=default_option, key=key)
        selected_values[key] = selected
        filtered_df = filtered_df[filtered_df[column].isin(selected)]

    return filtered_df, selected_values
