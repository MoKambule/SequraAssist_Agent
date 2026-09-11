import streamlit as st

def sidebar():
    st.sidebar.title("🦋 Sequra Assist")

    page = st.sidebar.radio(
        "Navigation",
        [
            "Home",
            "About",
            "Security Assessment",
            "Results"
            
        ]
    )
    return page
