from extractors.file_extractor import extract_text_from_file
from parser.preprocess import preprocess_resume_text
from parser.section_detector import detect_sections

file_path = "sample-resumes/My Resume Sample.pdf"

raw_text = extract_text_from_file(file_path)
processed = preprocess_resume_text(raw_text)
sections = detect_sections(processed["lines"])

print(f"---------- RAW TEXT ----------\n{raw_text}\n")
print(f"---------- CLEAN TEXT ----------\n{processed['clean_text']}\n")
print("\n---------- SECTIONS ----------")
for section, content in sections.items():
    print(f"\n--- {section.upper()} ---")
    for line in content:
        print(line)
