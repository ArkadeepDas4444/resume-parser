import re

EMAIL_PATTERN = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
PHONE_PATTERN = r"(?:\+?\d{1,3}[-.\s]?)?(?:\(?\d{3,5}\)?[-.\s]?)?[0-9\s-]{5,10}"
URL_PATTERN = r"https?://[^\s|,)]+|www\.[^\s|,)]+"
LINKEDIN_PATTERN = r"(?:https?://)?(?:www\.)?linkedin\.com/in/[A-Za-z0-9_-]+/?"
GITHUB_PATTERN = r"(?:https?://)?(?:www\.)?github\.com/[A-Za-z0-9_-]+/?"
LEETCODE_PATTERN = r"(?:https?://)?(?:www\.)?leetcode\.com/(?:u/)?[A-Za-z0-9_-]+/?"

def unique(items: list[str]) -> list[str]:
    seen = set()
    result = []

    for item in items:
        cleaned = item.strip().rstrip(".,;)")
        if cleaned and cleaned not in seen:
            seen.add(cleaned)
            result.append(cleaned)

    return result

def extract_phones(text: str) -> list[str]:
    candidates = re.findall(PHONE_PATTERN, text)

    phones = []
    for candidate in candidates:
        digits = re.sub(r"\D", "", candidate)

        if 10 <= len(digits) <= 13:
            phones.append(candidate.strip())

    return unique(phones)

def extract_contact_info(text: str) -> dict:
    urls = unique(re.findall(URL_PATTERN, text))
    linkedin = unique(re.findall(LINKEDIN_PATTERN, text, re.IGNORECASE))
    github = unique(re.findall(GITHUB_PATTERN, text, re.IGNORECASE))
    leetcode = unique(re.findall(LEETCODE_PATTERN, text, re.IGNORECASE))

    known_profile_urls = set(linkedin + github + leetcode)
    websites = [url for url in urls if url not in known_profile_urls]

    return {
        "emails": unique(re.findall(EMAIL_PATTERN, text)),
        "phones": extract_phones(text),
        "linkedin": linkedin,
        "github": github,
        "leetcode": leetcode,
        "websites": websites,
    }
