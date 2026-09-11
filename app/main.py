import streamlit as st

from sidebar import sidebar
from security_assessment import security_assessment
from about import about

st.set_page_config(
    page_title="Sequra Assist",
    page_icon="🦋",
    layout="wide"
)


page = sidebar() 

if page == "Home":

    st.title("🦋 Sequra Assist")

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

    st.title("Security Results")

    st.write(
        "Your security assessment results will appear here."
    )


