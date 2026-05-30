import re
from resources.degree_patterns import DEGREE_PATTERNS

SCORE_PATTERN = r"\b(?:CGPA|GPA)?\s*:?\s*(\d+(?:\.\d+)?)(?:\s*/\s*10|\s?%|\s*per\s?cent)?\b"
DATE_PATTERN = r"\b(?:19|20)\d{2}\s*(?:-|–|to)?\s*(?:Present|Current|(?:19|20)\d{2})?\b"

def extract_score(line: str):
    match = re.search(SCORE_PATTERN, line, re.IGNORECASE)
    return match.group(0) if match else None

def extract_date(line: str):
    match = re.search(DATE_PATTERN, line, re.IGNORECASE)
    return match.group(0) if match else None

def extract_education(education_lines: list[str]) -> list[dict]:
    education = []

    for line in education_lines:
        degree = None
        for pattern in DEGREE_PATTERNS:
            match = re.search(pattern, line, re.IGNORECASE)
            if match:
                degree = match.group()
                break

        if degree:
            education.append({
                "degree": degree,
                "score": extract_score(line),
                "date": extract_date(line),
                "raw_text": line
            })

    return education
