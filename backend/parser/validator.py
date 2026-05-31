def remove_empty_values(data):
    if isinstance(data, dict):
        return {
            key: remove_empty_values(value)
            for key, value in data.items()
            if value not in [None, "", [], {}]
        }

    if isinstance(data, list):
        return [
            remove_empty_values(item)
            for item in data
            if item not in [None, "", [], {}]
        ]

    return data

def deduplicate_list(items):
    seen = set()
    result = []

    for item in items:
        key = str(item).lower().strip()

        if key not in seen:
            seen.add(key)
            result.append(item)

    return result

def validate_resume_data(data: dict) -> dict:
    if "skills" in data and isinstance(data["skills"], list):
        data["skills"] = deduplicate_list(data["skills"])

    if "contact" in data and isinstance(data["contact"], dict):
        for key, value in data["contact"].items():
            if isinstance(value, list):
                data["contact"][key] = deduplicate_list(value)

    return remove_empty_values(data)
