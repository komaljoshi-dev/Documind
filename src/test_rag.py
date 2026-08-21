from indexer import create_document_index
from rag import ask_question


def main():
    pdf_paths = [
        "data/sample.pdf",
        "data/another.pdf"
    ]

    index, chunks = create_document_index(pdf_paths)

    query = "what do you mean by heartshield?"

    answer, sources = ask_question(query, index, chunks)

    print("\n---Answer---")
    print(answer)

    print("\nSources:")
    for source, page in sources:
        print(f"{source} - Page {page}")


if __name__ == "__main__":
    main()