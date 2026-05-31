import re

DATE_PATTERN = (
    r"\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|June?|July?|Aug(?:ust)?|Sept?(?:ember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)"
    r"[a-z]*\.?\s+\d{4}"
    r"(?:\s*(?:-|–|to)\s*"
    r"(?:Present|Curr(?:\.|ent)?|"
    r"(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|June?|July?|Aug(?:ust)?|Sept?(?:ember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)"
    r"[a-z]*\.?\s+\d{4}|\d{4}))?\b"
)

YEAR_PATTERN = r"[-–\s]*\(?(?:19|20)\)?\d\d"
LINK_HINTS = ["github", "website", "demo", "repo", "repository", "link"]

def extract_date(line: str):
    match = re.search(DATE_PATTERN, line, re.IGNORECASE)
    return match.group(0) if match else None

def is_project_title(line: str) -> bool:
    if not line.strip():
        return False
    if line.startswith("-"):
        return False

    # Project titles are usually short and often have a date nearby.
    if extract_date(line) or re.search(YEAR_PATTERN, line):
        return True

    return False

def clean_title(line: str, date: str | None) -> str:
    if date:
        line = line.replace(date, "")

    return line.strip(" -–|")

def extract_projects(project_lines: list[str]) -> list[dict]:
    projects = []
    current = None

    for line in project_lines:
        date = extract_date(line)

        if is_project_title(line):
            if current:
                projects.append(current)

            current = {
                "title": clean_title(line, date),
                "date": date,
                "description": [],
                "technologies": [],
                "links": [],
                "raw_lines": [line],
            }

        elif current:
            current["raw_lines"].append(line)

            lower_line = line.lower()

            if "technologies" in lower_line or "tech stack" in lower_line:
                tech_text = line.split(":", 1)[-1]
                current["technologies"] = [
                    item.strip()
                    for item in tech_text.split(",")
                    if item.strip()
                ]

            elif any(hint in lower_line for hint in LINK_HINTS):
                current["links"].append(line)

            else:
                current["description"].append(line)

    if current:
        projects.append(current)

    return projects
