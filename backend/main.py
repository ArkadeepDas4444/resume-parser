from extractors.file_extractor import extract_text_from_file
from parser.preprocess import preprocess_resume_text
from parser.section_detector import detect_sections
from parser.skills_extractor import extract_skills

file_path = "backend/sample_resumes/Admont-Resume-Green.docx"

raw_text = extract_text_from_file(file_path)
# print(f"\n---------- RAW TEXT ----------\n\n{raw_text}\n")

processed = preprocess_resume_text(raw_text)
# print(f"\n---------- CLEAN TEXT ----------\n\n{processed['clean_text']}\n")

sections = detect_sections(processed["lines"])
print("\n---------- SECTIONS ----------")
for section, content in sections.items():
    print(f"\n--- {section.title()} ---")
    for line in content:
        print(line)

skills = extract_skills("\n".join(sections["skills"]))
print(f"\n\n---------- SKILLS ----------\n\n{skills}\n")
