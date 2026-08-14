from pypdf import PdfReader

def extract_text(pdf_path):

    reader = PdfReader(pdf_path)
    text = ""
    NumberOfPages = len(reader.pages)

    for page in reader.pages:
        text += page.extract_text() or ""

    return text

def main():

    data = extract_text("data/sample.pdf")
    print("Extracted characters:", len(data))

if __name__ == "__main__":
    main()
