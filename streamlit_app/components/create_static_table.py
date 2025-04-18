import streamlit as st


def create_static_table(
    df,
    column_headers=None,
    bold_columns=None,
    percent_columns=None,
    float_columns=None,
    integer_columns=None,
    round_digits=2,
):
    """
    Renders a customizable HTML table in Streamlit.

    Args:
        df (pd.DataFrame): The DataFrame to render as an HTML table.
        column_headers (list[str], optional): Custom headers for the table.
        bold_columns (list[str], optional): Columns to render in bold.
        percent_columns (list[str], optional): Columns to format as percentages.
        float_columns (list[str], optional): Columns to round as decimals.
        integer_columns (list[str], optional): Columns to format as integers with thousand separators.
        round_digits (int, optional): Decimal precision for rounding.
    """
    bold_columns = bold_columns or []
    percent_columns = percent_columns or []
    float_columns = float_columns or []
    integer_columns = integer_columns or []

    headers = column_headers if column_headers else df.columns.tolist()

    # Generate header row
    header_html = "".join(
        [f"<th>{col.replace("_", " ").title()}</th>" for col in headers]
    )

    # Generate body rows
    table_rows = ""
    for _, row in df.iterrows():
        row_html = ""
        for col in df.columns:
            value = row[col]

            # Format percentages
            if col in percent_columns:
                value = f"{value:.{round_digits}f}%"
            # Format other numerics
            elif col in float_columns and isinstance(value, (int, float)):
                value = f"{value:,.{round_digits}f}"
            # Format integer columns
            elif col in integer_columns and isinstance(value, (int, float)):
                value = f"{int(value):,}"

            # Bold if necessary
            if col in bold_columns:
                value = f"<b>{value}</b>"

            row_html += f"<td>{value}</td>"
        table_rows += f"<tr>{row_html}</tr>"

    # Final HTML
    table_html = f"""
    <table class="styled-table">
        <thead>
            <tr>{header_html}</tr>
        </thead>
        <tbody>
            {table_rows}
        </tbody>
    </table>
    """

    st.markdown(table_html, unsafe_allow_html=True)
