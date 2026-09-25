def get_recommendations(assessment_data):

    recommendations = []
## Authentication
    if assessment_data["authentication_method"] != "No authentication":
        add_recommendation(
            recommendations,
            "Authentication Testing",
            "The application uses user authentication.",
            "High"
        )
## Authorisation
    if assessment_data["user_roles"] != "All users have the same permissions":
        recommendations.append(
            {
                "test": "Authorization Testing",
                "reason": "The application has different user permissions or roles.",
                "priority": "High"
            }
        )

    input_processes = [
        "User registration",
        "User login",
        "Payments or transactions",
        "File or document uploads",
        "Communication or messaging",
        "Orders or bookings",
        "Data processing"
    ]

    if any(process in assessment_data["core_processes"] for process in input_processes):
        recommendations.append(
            {
                "test": "Input Validation Testing",
                "reason": "The application supports processes that accept or process user input.",
                "priority": "Medium"
            }
        )
## API Exposure
    if assessment_data["application_exposure"] in [
        "Available through an API",
        "Multiple access methods"
    ]:
        recommendations.append(
            {
                "test": "API Security Testing",
                "reason": "The application is accessible through an API.",
                "priority": "Medium"
            }
        )

## Sensitive Data
    sensitive_data = [
        "Personal information",
        "Authentication credentials",
        "Financial information",
        "Payment information",
        "Health-related information",
        "Business or confidential information",
        "Uploaded documents"
    ]
    if any(data in assessment_data["data_types"] for data in sensitive_data):
        recommendations.append(
            {
                "test": "Sensitive Data Protection Testing",
                "reason": "The application handles sensitive or confidential information.",
                "priority": "High"
            }
        )
## Payments
    if "Payments or transactions" in assessment_data["core_processes"]:
        recommendations.append(
            {
                "test": "Payment Security Testing",
                "reason": "The application supports payments or financial transactions.",
                "priority": "High"
            }
        )

    return recommendations

# helper for recommendations 
def add_recommendation(recommendations, test, reason, priority):

    recommendations.append(
        {
            "test": test,
            "reason": reason,
            "priority": priority
        }
    )