import pdfplumber
import sys

def extract_with_pdfplumber(pdf_path, output_path=None):
    try:
        text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for i, page in enumerate(pdf.pages):
                text += f"--- Page {i+1} ---\n"
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
                else:
                    text += "[No text found on this page]\n"
        
        if output_path:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(text)
            return f"Success: Extracted to {output_path}"
        return text
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_plumber.py <pdf_path> [output_path]")
    else:
        path = sys.argv[1]
        out = sys.argv[2] if len(sys.argv) > 2 else None
        print(extract_with_pdfplumber(path, out))
