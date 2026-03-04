from pypdf import PdfReader
import sys

def extract_partial(pdf_path, pages_count=5):
    try:
        reader = PdfReader(pdf_path)
        text = ""
        actual_pages = min(len(reader.pages), pages_count)
        for i in range(actual_pages):
            text += f"--- Page {i+1} ---\n"
            text += reader.pages[i].extract_text() + "\n"
        return text
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_partial.py <pdf_path>")
    else:
        print(extract_partial(sys.argv[1]))
