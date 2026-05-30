from pathlib import Path

SKILLS_FILE = Path(__file__).resolve().parents[1] / "resources" / "skills.txt"

def load_skills(file_path: str) -> list[str]:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return [
                line.strip()
                for line in file
                if line.strip()
            ]

    except Exception as e:
        print(f"Error loading skills: {e}")
        return []

def extract_skills(text: str, skills_file: str | Path = SKILLS_FILE) -> list[str]:
    known_skills = load_skills(skills_file)
    found_skills = []

    text_lower = text.lower()

    for skill in known_skills:
        if skill.lower() in text_lower:
            found_skills.append(skill)

    return sorted(set(found_skills))
