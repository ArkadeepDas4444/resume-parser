# Resume Parser

A Python backend for parsing resumes into structured data. The project currently focuses on extraction and rule-based parsing using PDF/DOCX text extraction, preprocessing, section detection, regex patterns, and custom dictionaries.

The frontend is planned for later.

## Current Features

- Extract text from PDF resumes
- Extract text from DOCX resumes
- Route files automatically based on extension
- Preprocess extracted text
- Detect resume sections such as education, skills, projects, certifications, achievements, and experience
- Extract contact information such as email, phone, LinkedIn, GitHub, and websites
- Extract skills using a custom `skills.txt` dictionary
- Extract education, experience, projects, and candidate name using rule-based logic
- Validate and clean the final parsed output

## Project Structure

```text
resume-parser/
  backend/
    extractors/
      file_extractor.py
      pdf_extractor.py
      docx_extractor.py

    parser/
      preprocess.py
      section_detector.py
      contact_extractor.py
      name_extractor.py
      skills_extractor.py
      education_extractor.py
      experience_extractor.py
      projects_extractor.py
      validator.py

    resources/
      skills.txt
      degrees.txt
      job_titles.txt
      degree_patterns.py

    main.py

  frontend/
  README.md
  LICENSE
```

## Backend Pipeline

```text
resume file
    ↓
file_extractor.py
    ↓
pdf_extractor.py / docx_extractor.py
    ↓
preprocess.py
    ↓
section_detector.py
    ↓
field extractors
    ↓
validator.py
    ↓
structured resume data
```

## Setup

Create and activate a virtual environment:

```powershell
cd backend
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```powershell
pip install pdfplumber python-docx
```

If NLP features are added later, install spaCy and the required model separately.

## Running

From the `backend` directory:

```powershell
python main.py
```

The file path is currently configured inside `backend/main.py`.

Example:

```python
file_path = "sample_resumes/My Resume Sample.pdf"
```

Supported input formats:

- `.pdf`
- `.docx`

## Resource Files

The parser uses custom dictionaries in `backend/resources/`.

`skills.txt` should contain one skill per line:

```text
Python
Java
C++
React.js
LangChain
TensorFlow
```

`degrees.txt` should contain one degree or qualification per line:

```text
B.Tech
M.Tech
B.Sc
MBA
Ph.D
Class XII
Senior Secondary
```

## Notes and Limitations

- The parser is currently rule-based, not LLM-based.
- It works best with ATS-friendly resumes.
- Single-column resumes generally extract better than complex multi-column layouts.
- Fancy Canva-style resumes may produce noisy text because PDF layout extraction is difficult.
- Scanned/image-only PDFs are not currently supported unless OCR is added.
- Extraction quality depends heavily on the raw text produced by the PDF/DOCX extractor.

## Planned Improvements

- Improve multi-column PDF extraction
- Add OCR fallback for scanned PDFs
- Improve education and experience extraction
- Add stronger validation and confidence scoring
- Add API endpoints
- Build frontend
