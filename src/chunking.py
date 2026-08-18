def create_chunks(pages,chunk_size=150, overlap=30):

    chunks = []
    for page in pages:

        words = page["text"].split()
        start = 0

        while start < len(words):
            end = start + chunk_size

            chunk = " ".join(words[start : end])
            chunks.append({
                "text": chunk,
                "page": page["page"]
            })

            start += chunk_size-overlap

    return chunks 