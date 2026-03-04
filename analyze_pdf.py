from pypdf import PdfReader
import sys

def analyze_pdf(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        info = {
            "pages": len(reader.pages),
            "metadata": reader.metadata,
        }
        text_sample = ""
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text and text.strip():
                text_sample += f"--- Page {i+1} ---\n{text[:1000]}\n"
        return info, text_sample
    except Exception as e:
        return str(e), ""

if __name__ == "__main__":
    path = sys.argv[1]
    info, sample = analyze_pdf(path)
    print(f"Info: {info}")
    if sample:
        print(f"Sample:\n{sample}")
    else:
        print("No text sample found.")
