*** Sequra Assist — Project Brief ***

**1. Problem Statement**

Small businesses, startups, and early-stage companies may have access to security testing tools but often lack the specialised security expertise, time, and resources needed to determine what should be tested first and which security findings require the most attention.

Existing security tools can identify technical vulnerabilities, but technical findings alone do not always provide enough business context to determine their importance or the appropriate next action.

Sequra Assist aims to address this gap by acting as an intelligent security and quality risk management assistant. It uses business and application context to help teams identify relevant security risks, select appropriate tests, analyse findings, and prioritise actions based on potential business impact.

**2. Target Users**

The primary target users are:

* Startups and small businesses with limited security resources
* Incubation-stage companies developing new digital products
* Small development teams without dedicated security specialists
* Developers and QA professionals who need guidance on security testing
* Teams that use security tools but need help interpreting and prioritising their results

The initial focus is on organisations that need practical security guidance without requiring a dedicated security team or extensive security expertise due to budget constraints and limited development teams.

**3. Project Goals**

The goal of Sequra Assist is to demonstrate how an AI-powered assistant can improve security testing decision-making by connecting business context with technical security testing.

* Understand the security context of an organisation and its application
* Identify and prioritise potential security risks
* Recommend relevant security tests based on the application's context
* Integrate with existing security testing tools rather than replacing them
* Analyse and normalise security findings from different tools
* Prioritise findings according to technical severity and business impact
* Translate technical security findings into clear, actionable recommendations
* Provide a simple interface that allows users to understand what should be tested and what should be addressed first

**4. MVP Scope**

The MVP will focus on demonstrating the core decision-making workflow of Sequra Assist rather than building a complete enterprise security platform.

*In Scope*

The MVP will include:

. A Streamlit-based dashboard for interacting with Sequra Assist.
. A business context questionnaire that captures information about the organisation and application.
. A risk assessment component that evaluates the provided context.
. A security test catalogue containing relevant security testing categories.
. A recommendation engine that determines which security tests should be prioritised.
. An AI agent that helps interpret the business context and security information.
. Integration with selected security testing tools such as OWASP ZAP, Semgrep, and Trivy.
. A standardised finding format for security results from different tools.
. Analysis of security findings.
. Risk prioritisation based on technical and business context.
. Clear recommendations explaining what the user should address first.

*Out of Scope for the MVP*

The following will not be required for the initial prototype:

* A complete enterprise security management platform
* Continuous production monitoring
* Full automated penetration testing
* Support for every security testing tool
* Full CI/CD automation
* Advanced user authentication and account management
* Large-scale cloud deployment
* Complete vulnerability management lifecycle automation

These capabilities may be considered as future extensions after the MVP has demonstrated the core concept.

**5. MVP Success Criteria**

The MVP should demonstrate the following end-to-end workflow:

Business Context
→ Risk Assessment
→ Security Test Recommendation
→ Security Testing
→ Finding Analysis
→ Risk Prioritisation
→ Actionable Recommendation

A successful demonstration should show that Sequra Assist can take information about an application, determine relevant security testing priorities, process security findings, and explain which risks the organisation should address first.

**6. Project Focus**

The central focus of the project is not to create another security scanner.

Instead, Sequra Assist will provide an intelligent decision-making layer around existing security tools.

The key questions the system should help answer are:

*What should we test?*
*Why should we test it?*
*What do the findings mean for the business?*
*What should we fix first?*


