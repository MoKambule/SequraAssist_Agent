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
        "Tell us about your business, application, and the processes "
        "you want to protect."
    )

    st.divider()

    # -----------------------------------------
    # 1. USER GOALS
    # -----------------------------------------

    st.header("1. Your Goals")

    application_purpose = st.selectbox(
        "What is the main purpose of your application?",
        [
            "Selling products or services",
            "Managing customers",
            "Processing payments",
            "Managing internal business operations",
            "Providing information or content",
            "Connecting users or businesses",
            "Other"
        ],
        width=500,
    )

    if application_purpose == "Other":
        application_purpose_other = st.text_input(
            "Please describe the main purpose of your application."
        )

    primary_users = st.selectbox(
        "Who are the main users of the application?",
        [
            "Customers",
            "Employees",
            "Business partners",
            "Administrators",
            "Students or learners",
            "General public",
            "Multiple user groups",
            "Other"
        ], 
        width=500,
    )

    if primary_users == "Other":
        primary_users_other = st.text_input(
            "Please describe who uses the application.",width=500
        )

    # -----------------------------------------
    # 2. CORE PROCESSES
    # -----------------------------------------

    st.header("2. Core Business Processes")

    core_process = st.multiselect(
        "Which important processes does the application support?",
        [
            "User registration",
            "User login",
            "Payments or transactions",
            "Customer information management",
            "File or document uploads",
            "Communication or messaging",
            "Orders or bookings",
            "Reporting",
            "Data processing",
            "Other"
        ],
        width=500,
    )

    if "Other" in core_process:
        core_process_other = st.text_input(
            "Please describe the other important process.",width=500
        )

    business_impact = st.selectbox(
        "What would be the impact if this application stopped working?",
        [
            "Little or no impact",
            "Some business operations would be affected",
            "Customers would be affected",
            "Major business operations would stop",
            "The business could suffer significant financial or reputational damage"
        ],
        width=500,
    )

    # -----------------------------------------
    # 3. DATA RULES
    # -----------------------------------------

    st.header("3. Data")

    data_types = st.multiselect(
        "What types of information does the application handle?",
        [
            "Basic customer information",
            "Personal information",
            "Authentication credentials",
            "Financial information",
            "Payment information",
            "Business or confidential information",
            "Health-related information",
            "Uploaded documents",
            "No sensitive information",
            "Other"
        ],
        width=500,
    )

    if "Other" in data_types:
        data_types_other = st.text_input(
            "Please describe the other type of information.",width=500
        )

    data_storage = st.selectbox(
        "Where is the application's important data stored?",
        [
            "Application database",
            "Cloud database",
            "Third-party service",
            "File storage",
            "Multiple locations",
            "Other"
        ],
        width=500,
    )

    if data_storage == "Other":
        data_storage_other = st.text_input(
            "Please describe where the data is stored.",width=500
        )

    data_access = st.selectbox(
        "Who should be able to access the application's data?",
        [
            "All users",
            "Registered users",
            "Employees",
            "Administrators only",
            "Different users have different access levels",
            "Other"
        ],
        width=500,
    )

    if data_access == "Other":
        data_access_other = st.text_input(
            "Please describe who should have access.",width=500
        )

    # -----------------------------------------
    # 4. RISK & EXPOSURE
    # -----------------------------------------

    st.header("4. Risk & Exposure")

    application_exposure = st.selectbox(
        "How can users access the application?",
        [
            "Publicly available on the internet",
            "Available only to registered users",
            "Available to employees through the internet",
            "Internal company network only",
            "Available through an API",
            "Multiple access methods",
            "Other"
        ],
        width=500,
    )

    if application_exposure == "Other":
        application_exposure_other = st.text_input(
            "Please describe how users access the application.",width=500
        )

    authentication_method = st.selectbox(
        "How do users authenticate with the application?",
        [
            "Username and password",
            "Email and password",
            "Single Sign-On (SSO)",
            "Social login",
            "Multi-factor authentication (MFA)",
            "No authentication",
            "Multiple authentication methods",
            "Other"
        ],
        width=500,
    )

    if authentication_method == "Other":
        authentication_method_other = st.text_input(
            "Please describe the authentication method.",width=500
        )

    user_roles = st.selectbox(
        "How are user permissions managed?",
        [
            "All users have the same permissions",
            "Users have different roles",
            "Administrators have additional permissions",
            "Access is based on specific resources",
            "Multiple permission levels",
            "Other"
        ],width=500,
    )

    if user_roles == "Other":
        user_roles_other = st.text_input(
            "Please describe how permissions are managed.",width=500
        )

    risk_consequence = st.selectbox(
        "What would be the most serious consequence of a security incident?",
        [
            "Temporary service disruption",
            "Loss of customer information",
            "Unauthorised access to accounts",
            "Financial loss",
            "Loss of confidential business information",
            "Reputational damage",
            "Multiple consequences",
            "Other"
        ],
        width=500,
    )

    if risk_consequence == "Other":
        risk_consequence_other = st.text_input(
            "Please describe the potential consequence.",width=500
        )

    st.divider()

    if st.button("Assess Risk", type="primary"):

        st.success("Business context submitted successfully!")

        st.write("### Assessment Information")

        st.write("**Application Purpose:**", application_purpose)
        st.write("**Primary Users:**", primary_users)
        st.write("**Core Processes:**", core_process)
        st.write("**Business Impact:**", business_impact)
        st.write("**Data Types:**", data_types)
        st.write("**Data Storage:**", data_storage)
        st.write("**Data Access:**", data_access)
        st.write("**Application Exposure:**", application_exposure)
        st.write("**Authentication:**", authentication_method)
        st.write("**User Roles:**", user_roles)
        st.write("**Potential Consequence:**", risk_consequence)



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