from datetime import datetime


def create_downloadable_report(profile, role, experience, interview_type, final_report):
    today = datetime.now().strftime("%d %B %Y")

    return f"""
AI Interview Simulator - Professional Report

Date: {today}

Candidate Name: {profile['full_name']}
Field: {profile['field']}
Qualification: {profile['qualification']}
Skills: {profile['skills']}
Target Role: {role}
Experience Level: {experience}
Interview Type: {interview_type}

--------------------------------------------------

{final_report}
"""