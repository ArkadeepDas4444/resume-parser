import re
from parser.contact_extractor import EMAIL_PATTERN, PHONE_PATTERN, URL_PATTERN

def is_contact_line(line: str) -> bool:
    return (
        re.search(EMAIL_PATTERN, line) is not None
        or re.search(PHONE_PATTERN, line) is not None
        or re.search(URL_PATTERN, line, re.IGNORECASE) is not None
    )

def is_probable_name(line: str) -> bool:
    words = line.strip().split()
    if not len(words) <= 4:
        return False
    if is_contact_line(line):
        return False
    if any(char.isdigit() for char in line):
        return False

    return True

def extract_name(header_lines: list[str]) -> str | None:
    for line in header_lines[:5]:
        clean_line = line.strip()
        if is_probable_name(clean_line):
            return clean_line

    return None
