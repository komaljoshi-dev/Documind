import faiss
from ingest import extract_text
from chunking import create_chunks
from embeddings import create_chunk_embeddings

def build_index(embeddings):
  dimension = embeddings.shape[1]
  index = faiss.IndexFlatL2(dimension) #we told faiss we need an index which stores 384 dimensions
  index.add(embeddings)
  return index

def create_document_index(pdf_path):
  data = extract_text(pdf_path)
  chunks = create_chunks(data)
  embeddings = create_chunk_embeddings(chunks)
  index = build_index(embeddings)

  return index, chunks