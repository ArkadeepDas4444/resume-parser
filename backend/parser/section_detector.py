import re

SECTION_KEYWORDS = {
    "summary": ["summary", "profile", "objective"],
    "education": ["education", "academic qualification"],
    "experience": ["experience", "employment", "work history", "internship", "internships"],
    "positions": ["positions", "positions of responsibility", "responsibility"],
    "skills": ["skills", "technical skills", "technologies"],
    "interests": ["interests"],
    "projects": ["project", "projects"],
    "certifications_and_courses": ["certification", "certifications", "certificates", "training", "coursework", "courses"],
    "achievements": ["achievement", "achievements", "awards", "honors"],
    "competitions": ["competition", "competitions", "hackathons"],
    # "languages": ["languages"],
    "activities": ["hobbies", "activities", "extracurricular", "extracurriculars"]
}

def normalize_line(line: str) -> str:
    line = line.lower()
    line = re.sub(r"[^a-z0-9\s&]", " ", line)
    line = re.sub(r"\s+", " ", line)
    return line.strip()

def is_probable_heading(line: str) -> bool:
    stripped = line.strip()

    if not stripped:
        return False

    # Avoid long normal sentences and lines starting is small letters
    if len(stripped.split()) > 6 or len(stripped) > 30 or stripped[0].islower():
        return False

    return True

def detect_section(line: str):
    if not is_probable_heading(line):
        return None

    normalized = normalize_line(line)

    for section_name, keywords in SECTION_KEYWORDS.items():
        for keyword in keywords:
            if keyword in normalized:
                return section_name

    return None

def detect_sections(lines: list[str]) -> dict:
    sections = {}
    current_section = "header"
    sections[current_section] = []

    for line in lines:
        detected_section = detect_section(line)

        if detected_section:
            current_section = detected_section
            sections.setdefault(current_section, [])
        else:
            sections[current_section].append(line)

    return sections
