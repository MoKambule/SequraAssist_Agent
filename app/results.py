import streamlit as st


def show_results():

    st.header("Security Risk Overview")

    if "assessment_completed" not in st.session_state:

        st.warning(
            "Please complete the Security Assessment first."
        )
        return

    st.success(
        "Your assessment has been completed."
    )

    st.write(
        "The information below is based on your submitted "
        "business and application context."
    )

    assessment_data = st.session_state["assessment_data"]
    risk_result = st.session_state["risk_result"]
    recommendations = st.session_state["recommendations"]

    st.divider()

    st.subheader("Overall Risk")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="Risk Level",
            value=risk_result["level"]
        )
    with col2:
       st.metric(
            label="Risk Score",
            value=f'{risk_result["score"]} / 100'
        )

   

    st.divider()

    st.subheader("Recommended Security Tests")
    for recommendation in recommendations:
        st.write(f"✓ {recommendation}")


    st.divider()

    st.subheader("Priority Actions")

    st.markdown(
        """
        **1. 🔴 Test authentication controls**

        **2. 🟠 Test authorization and user permissions**

        **3. 🟡 Test input validation**

        **4. 🟡 Review API security**
        """
    )

    st.divider()

   