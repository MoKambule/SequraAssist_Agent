import streamlit as st

st.set_page_config(
    page_title="Sequra Assist",
    page_icon="🦋",
    layout="wide"
)

st.sidebar.title("🦋 Sequra Assist")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Security Assessment",
        "Results",
        "About"
    ]
)

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


elif page == "Security Assessment":

    st.title("Security Assessment")

    st.write(
        "Tell us about your business and application."
    )


elif page == "Results":

    st.title("Security Results")

    st.write(
        "Your security assessment results will appear here."
    )


elif page == "About":

    st.title("About Sequra Assist")

    st.write(
        "Sequra Assist is an AI-powered security risk "
        "management assistant designed to help small teams "
        "make better security testing decisions."
    )