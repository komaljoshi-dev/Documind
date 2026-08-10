from pypdf import PdfReader

def extract_text(pdf_path):

    reader = PdfReader(pdf_path)
    text = ""
    print(len(reader.pages))

    for page in reader.pages:
        text += page.extract_text() or ""

    return text

def main():

    data = extract_text("data/sample.pdf")
    print(data)

if __name__ == "__main__":
    main()
