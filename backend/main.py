from extractors.file_extractor import extract_text_from_file
from parser.preprocess import preprocess_resume_text
from parser.section_detector import detect_sections
from parser.skills_extractor import extract_skills
from parser.education_extractor import extract_education
from parser.contact_extractor import extract_contact_info
from parser.experience_extractor import extract_experience
from parser.projects_extractor import extract_projects
from parser.name_extractor import extract_name

file_path = "backend/sample_resumes/Quebec-Resume-Light-Blue.docx"

raw_text = extract_text_from_file(file_path)
# print("\n---------- RAW TEXT ----------\n")
# print(raw_text + "\n")

processed = preprocess_resume_text(raw_text)
print("\n---------- CLEAN TEXT ----------\n")
print(f"{processed['clean_text']}\n")

sections = detect_sections(processed["lines"])
print("\n---------- SECTIONS ----------")
for section, content in sections.items():
    print(f"\n--- {section.title()} ---")
    for line in content:
        print(line)

print()

skills = extract_skills("\n".join(sections.get("skills", [])))
print("\n---------- SKILLS ----------\n")
print(f"{skills}\n")

education = extract_education(sections.get("education", []))
print("\n---------- EDUCATION DATA ----------\n")
print(f"{education}\n")

contact_info = extract_contact_info("\n".join(sections.get("header", [])))
print("\n---------- CONTACT INFO ----------\n")
print(f"{contact_info}\n")

experience_lines = sections.get("experience", []) + sections.get("positions", [])
experience = extract_experience(experience_lines)
print("\n---------- EXPERIENCE ----------\n")
print(f"{experience}\n")

projects = extract_projects(sections.get("projects", []))
print("\n---------- PROJECTS ----------\n")
print(f"{projects}\n")

name = extract_name(sections.get("header", []))
print("\n---------- NAME ----------\n")
print(f"{name}\n")
