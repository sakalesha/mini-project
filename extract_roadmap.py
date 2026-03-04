from pdfminer.high_level import extract_text
import sys

def get_text(pdf_path, output_path=None):
    try:
        text = extract_text(pdf_path)
        if output_path:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(text)
            return f"Success: Extracted to {output_path}"
        return text
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_roadmap.py <pdf_path> [output_path]")
    else:
        path = sys.argv[1]
        out = sys.argv[2] if len(sys.argv) > 2 else None
        print(get_text(path, out))
