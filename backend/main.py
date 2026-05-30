from extractors.file_extractor import extract_text_from_file
from parser.preprocess import preprocess_resume_text
from parser.section_detector import detect_sections
from parser.skills_extractor import extract_skills
from parser.education_extractor import extract_education

file_path = "backend/sample_resumes/Resume with Table IITG.pdf"

raw_text = extract_text_from_file(file_path)
# print("\n---------- RAW TEXT ----------\n")
# print(raw_text + "\n")

processed = preprocess_resume_text(raw_text)
print("\n---------- CLEAN TEXT ----------\n")
print(processed['clean_text'] + "\n")

sections = detect_sections(processed["lines"])
print("\n---------- SECTIONS ----------")
for section, content in sections.items():
    print(f"\n--- {section.title()} ---")
    for line in content:
        print(line)

print()

skills = extract_skills("\n".join(sections.get("skills", "")))
print("\n---------- SKILLS ----------\n")
print(skills + "\n")

education = extract_education(sections.get("education", []))
print(f"\n---------- EDUCATION DATA ----------\n\n{education}\n")
