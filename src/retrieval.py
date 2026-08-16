from indexer import create_document_index
from embeddings import create_embeddings
from generator import generate_answer

def retrieve(query, index, chunks, k=3, threshold=1.5):
  query_embedding = create_embeddings([query])
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
    index,chunks = create_document_index("data/sample.pdf")

    query = "How does the application manage global state?"
    results = retrieve(query, index, chunks)

    if not results:
       print("\nThe answer was not found in the document.")
    else:
      retrieved_chunks = [result["chunk"] for result in results]
      answer = generate_answer(query, retrieved_chunks)
      
      print("\n---Answer---")
      print(answer)

if __name__ == "__main__":
    main()