import faiss
from ingest import extract_text
from chunking import create_chunks
from embeddings import create_embeddings
from generator import generate_answer

def build_index(embeddings):
  dimension = embeddings.shape[1]
  index = faiss.IndexFlatL2(dimension) #we told faiss we need an index which stores 384 dimensions
  index.add(embeddings)
  return index

def retrieve(query, index, chunks, k=3):
  query_embedding = create_embeddings([query])
  distances, indices = index.search(query_embedding, k)

  retrieved_chunks = []
  for i in indices[0]:
    retrieved_chunks.append(chunks[i])

  return retrieved_chunks

def main():

    data = extract_text("data/sample.pdf")#extracts text from pdf
    chunks = create_chunks(data)#creates chunks from text
    embeddings = create_embeddings(chunks)

    index = build_index(embeddings)

    query = "How does the application manage global state?"
    results = retrieve(query, index, chunks)

    answer = generate_answer(query, results)
    print(answer)

if __name__ == "__main__":
    main()