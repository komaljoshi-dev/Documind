from pypdf import PdfReader

def extract_text(pdf_path):

    reader = PdfReader(pdf_path)
    pages = []
    
    for page_number, page in enumerate(reader.pages,start=1):
        text = page.extract_text() or ""

        pages.append({
            "page" : page_number,
            "text" : text
        })

    return pages

def main():

    pages = extract_text("data/sample.pdf")
    print("first page :", pages[0]["text"][:200])

if __name__ == "__main__":
    main()