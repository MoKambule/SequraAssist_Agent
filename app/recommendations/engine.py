def get_recommendations(assessment_data):

    return [
        {
            "test": "Authentication Testing",
            "reason": "The application uses user authentication.",
            "priority": "High"
        },
        {
            "test": "Authorization Testing",
            "reason": "The application has different user access levels.",
            "priority": "High"
        },
        {
            "test": "Input Validation Testing",
            "reason": "The application processes user input.",
            "priority": "Medium"
        },
               {
            "test": "API Security Testing",
            "reason": "The application may expose functionality through APIs.",
            "priority": "Medium"
        }
    ]