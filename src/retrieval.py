import faiss
from ingest import extract_text
from chunking import create_chunks
from embeddings import create_embeddings

data = extract_text("data/sample.pdf") #extracts text from pdf
chunks = create_chunks(data) #creates chunks from text
embeddings = create_embeddings(chunks)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension) #we told faiss we need an index which stores 384 dimensions

index.add(embeddings)
print(index.ntotal)

query = " what is this project about?"

query_embedding = create_embeddings([query])

distances, indices = index.search(query_embedding,3)

print("Distances:", distances)
print("Indices:", indices)

for i in indices[0]:
  print("\n--- Retrieved chunk ---")
  print(chunks[i])