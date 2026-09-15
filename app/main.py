import streamlit as st

from sidebar import sidebar
from security_assessment import security_assessment
from about import about
from header import show_header
from results import show_results

st.set_page_config(
    page_title="Sequra Assist",
    page_icon="🦋",
    layout="wide"
)

show_header()
page = sidebar() 


if page == "Home":


    st.subheader(
        "AI-Powered Security & Quality Risk Management"
    )


    st.divider()

    st.header("Welcome")

    st.write(
        "Sequra Assist helps small teams understand their "
        "security risks, identify what should be tested, "
        "and prioritise security findings."
    )

    st.button("Start Security Assessment")

elif page == "About":

   about()

elif page == "Security Assessment":

    security_assessment()

elif page == "Results":
    show_results()


