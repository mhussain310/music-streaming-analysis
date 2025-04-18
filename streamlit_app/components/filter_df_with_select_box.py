import streamlit as st


def filter_df_with_select_box(
    df,
    column_filter,
    filter_label,
    keyname,
    multi_select=False,
    multi_select_filter="",
    multi_select_label="",
    multi_select_keyname="",
):
    select_box_list = sorted(df[column_filter].unique())
    select_box_current_selected = st.selectbox(
        f"{filter_label}", select_box_list, key=keyname
    )

    if multi_select:
        multi_select_list = sorted(df[multi_select_filter].unique().tolist())
        multi_select_current_selected = st.multiselect(
            multi_select_label,
            multi_select_list,
            default=multi_select_list[0:5],
            key=multi_select_keyname,
        )
        filtered_df = df[
            df[multi_select_filter].isin(multi_select_current_selected)
            & df[column_filter].isin([select_box_current_selected])
        ]
        return (filtered_df, select_box_current_selected, multi_select_current_selected)
    else:
        # Filter dataframe based on selected genre
        filtered_df = df[df[column_filter] == select_box_current_selected]

        return (filtered_df, select_box_current_selected)
