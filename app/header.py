import streamlit as st


def show_header():
    st.markdown(
        """
        <style>
        .block-container{
        padding-top: 1.5rem
        }
        </style>
       """,
    unsafe_allow_html = True
    )
    st.title("🦋 Sequra Assist")