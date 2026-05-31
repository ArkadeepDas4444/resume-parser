import re

DURATION_PATTERN = (
    r"\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|June?|July?|Aug(?:ust)?|Sept?(?:ember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)"
    r"[a-z]*\.?\s+\d{4}\s*(?:-|–|to)\s*"
    r"(?:Present|Curr(?:\.|ent)?|"
    r"(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|June?|July?|Aug(?:ust)?|Sept?(?:ember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)[a-z]*\.?\s+\d{4}|\d{4})\b"
)

def extract_duration(line: str):
    match = re.search(DURATION_PATTERN, line, re.IGNORECASE)
    return match.group(0) if match else None

def extract_experience(experience_lines: list[str]) -> list[dict]:
    experiences = []
    current = None

    for line in experience_lines:
        duration = extract_duration(line)

        if duration:
            if current:
                experiences.append(current)

            title_part = line.replace(duration, "").strip(" -–|")

            current = {
                "title": title_part or None,
                "organization": None,
                "duration": duration,
                "description": [],
                "raw_lines": [line],
            }

        elif current:
            current["description"].append(line)
            current["raw_lines"].append(line)

    if current:
        experiences.append(current)

    return experiences
