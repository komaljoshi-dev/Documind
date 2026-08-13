from sentence_transformers import SentenceTransformer


model = SentenceTransformer("all-MiniLM-L6-v2")

def create_embeddings(chunks):
    return model.encode(chunks)

#print("Number of chunks:",len(chunks))
#print("Embeddings shape:",embeddings.shape)

