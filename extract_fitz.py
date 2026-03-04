import fitz  # PyMuPDF
import sys

def extract_text_fitz(pdf_path, output_path=None):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += f"--- Page {page.number + 1} ---\n"
            text += page.get_text() + "\n"
        
        if output_path:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(text)
            return f"Success: Extracted to {output_path}"
        return text
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_fitz.py <pdf_path> [output_path]")
    else:
        path = sys.argv[1]
        out = sys.argv[2] if len(sys.argv) > 2 else None
        print(extract_text_fitz(path, out))
