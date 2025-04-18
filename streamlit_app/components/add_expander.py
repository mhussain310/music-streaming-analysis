import streamlit as st


def sql_query_result_expander(df):
    st.markdown(
        """
        <style>
            .st-emotion-cache-1h9usn1 {
                background-color: #ffffff;
                font-weight: bold;
                border-radius: 0;
            }
            .st-emotion-cache-4rp1ik:hover {
              color: #000000;
            }
            .st-emotion-cache-4rp1ik:hover svg {
              fill: #000000;
            }
            .st-emotion-cache-1clstc5 {
                padding-top: 1rem;
                background-color: #f5f5f5;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    with st.expander("Expand to view SQL query output"):
        st.write(df)
