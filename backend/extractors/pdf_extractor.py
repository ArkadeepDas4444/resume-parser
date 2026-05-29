import pdfplumber

def extract_text_from_pdf(pdf_path):
    extracted_text = []

    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()

                if page_text:
                    extracted_text.append(page_text)

        return "\n".join(extracted_text).strip()

    except Exception as e:
        print(f"Error extracting PDF: {e}")
        return None
