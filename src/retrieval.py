from indexer import create_document_index
from embeddings import create_query_embedding
from generator import generate_answer

def retrieve(query, index, chunks, k=3, threshold=1.5):
  query_embedding = create_query_embedding(query)
  distances, indices = index.search(query_embedding, k)

  results = []

  for i, distance in zip(indices[0], distances[0]):
      if distance <= threshold:
        results.append({
            "chunk": chunks[i],
            "distance": distance
        })
  return results

def main():
    pdf_paths = [
       "data/sample.pdf",
       "data/another.pdf"
    ]
    index,chunks = create_document_index(pdf_paths)
    print("total chunks", len(chunks))
    for chunk in chunks:
      print(chunk["source"], chunk["page"])
    query = "How does the application manage global state?"
    results = retrieve(query, index, chunks)

    if not results:
       print("\nThe answer was not found in the document.")
    else:

      retrieved_chunks = [result["chunk"]["text"] for result in results]
      answer = generate_answer(query, retrieved_chunks)
      
      print("\n---Answer---")
      print(answer)

      sources = sorted(
        set(
          (result["chunk"]["source"] ,result["chunk"]["page"])
          for result in results
          )
        )

      print("\nSources: ")
      for source,page in sources:
        print(f"{source} - Page {page}")

if __name__ == "__main__":
  main()