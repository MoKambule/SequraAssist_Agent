import streamlit as st


def show_results():

    st.header("Security Risk Overview")

    if "assessment_completed" not in st.session_state:

        st.warning(
            "Please complete the Security Assessment first."
        )

        st.info(
            "Use the sidebar to open the Security Assessment page."
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

    st.divider()

    st.subheader("Overall Risk")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="Risk Level",
            value="HIGH"
        )

    with col2:
        st.metric(
            label="Risk Score",
            value="78 / 100"
        )

    with col3:
        st.metric(
            label="Priority Areas",
            value="4"
        )

    st.divider()

    st.subheader("Submitted Assessment Information")

    st.write(
        "**Application Purpose:**",
        assessment_data["application_purpose"]
    )

    st.write(
        "**Primary Users:**",
        assessment_data["primary_users"]
    )

    st.write(
        "**Core Processes:**",
        assessment_data["core_processes"]
    )

    st.write(
        "**Business Impact:**",
        assessment_data["business_impact"]
    )

    st.write(
        "**Data Types:**",
        assessment_data["data_types"]
    )

    st.write(
        "**Application Exposure:**",
        assessment_data["application_exposure"]
    )

    st.write(
        "**Authentication Method:**",
        assessment_data["authentication_method"]
    )

    st.write(
        "**Potential Consequence:**",
        assessment_data["risk_consequence"]
    )

    st.divider()

    st.subheader("Recommended Security Tests")

    st.success("✓ Authentication Testing")
    st.warning("✓ Authorization Testing")
    st.warning("✓ Input Validation Testing")
    st.info("✓ API Security Testing")

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

    st.caption(
        "The risk score and recommendations are currently "
        "placeholder data for the prototype."
    )