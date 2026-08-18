from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_chunk_embeddings(chunks):
    texts = [ chunk["text"] for chunk in chunks]

    return model.encode(texts)

def create_query_embedding(query):
    return model.encode([query])