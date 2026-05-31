import re

BULLET_CHARS = ["•", "●", "▪", "▫", "◦", "‣", "∙", "–", "—"]

def remove_page_numbers(text: str) -> str:
    lines = []

    for line in text.split("\n"):
        stripped = line.strip()

        # Page 1
        # Page 1 of 2
        # 1 / 2
        # 1 of 2
        if re.fullmatch(r"[-–\s]*page\s+\d+(\s+of\s+\d+)?[-–\s]*", stripped, re.IGNORECASE):
            continue
        if re.fullmatch(r"[-–\s]*\d+\s*(/|of)\s*\d+[-–\s]*", stripped, re.IGNORECASE):
            continue

        lines.append(line)

    return "\n".join(lines)

def normalize_bullets(text: str) -> str:
    for bullet in BULLET_CHARS:
        text = text.replace(bullet, "-")
    return text

def normalize_whitespace(text: str) -> str:
    # Normalize Windows/Mac line endings
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # Replace tabs with spaces
    text = text.replace("\t", " ")

    # Remove extra spaces inside each line
    lines = []
    for line in text.split("\n"):
        line = re.sub(r"[ ]{2,}", " ", line)
        lines.append(line.strip())

    return "\n".join(lines)

def remove_excess_blank_lines(text: str) -> str:
    # Keep paragraph/section breaks, but avoid huge gaps
    return re.sub(r"\n{3,}", "\n\n", text)

def clean_text(text: str) -> str:
    if not text:
        return ""

    text = remove_page_numbers(text)
    text = normalize_bullets(text)
    text = normalize_whitespace(text)
    text = remove_excess_blank_lines(text)

    return text.strip()

def get_lines(text: str) -> list[str]:
    return [
        line.strip()
        for line in text.split("\n")
        if line.strip()
    ]

def preprocess_resume_text(raw_text: str) -> dict:
    cleaned = clean_text(raw_text)

    return {
        "raw_text": raw_text,
        "clean_text": cleaned,
        "lines": get_lines(cleaned),
    }
