import re


def extract_score(feedback, score_name):
    pattern = rf"{score_name}:\s*(\d+)"
    match = re.search(pattern, feedback, re.IGNORECASE)

    if match:
        return int(match.group(1))

    return 0


def calculate_average_scores(feedback_list):
    if not feedback_list:
        return {
            "communication": 0,
            "technical": 0,
            "confidence": 0,
            "overall": 0
        }

    return {
        "communication": round(sum(extract_score(f, "Communication") for f in feedback_list) / len(feedback_list), 1),
        "technical": round(sum(extract_score(f, "Technical") for f in feedback_list) / len(feedback_list), 1),
        "confidence": round(sum(extract_score(f, "Confidence") for f in feedback_list) / len(feedback_list), 1),
        "overall": round(sum(extract_score(f, "Overall") for f in feedback_list) / len(feedback_list), 1)
    }