from pypdf import PdfReader
import sys

def extract_text(pdf_path, output_path=None):
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        
        if output_path:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(text)
            return f"Success: Extracted to {output_path}"
        return text
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_pdf.py <pdf_path> [output_path]")
    else:
        path = sys.argv[1]
        out = sys.argv[2] if len(sys.argv) > 2 else None
        result = extract_text(path, out)
        if out:
            print(result)
        else:
            print(result)
