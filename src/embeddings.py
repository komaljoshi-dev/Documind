from ingest import extract_text
from chunking import create_chunks

from sentence_transformers import SentenceTransformer


model = SentenceTransformer("all-MiniLM-L6-v2")

data = extract_text("data/sample.pdf") #extracts text from pdf
chunks = create_chunks(data) #creates chunks from text
embeddings = model.encode(chunks) #creates embeddings

print("Number of chunks:",len(chunks))
print("Embeddings shape:",embeddings.shape)

