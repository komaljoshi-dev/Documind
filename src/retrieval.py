from .embeddings import create_query_embedding

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