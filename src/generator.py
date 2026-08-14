import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_answer(query, retrieved_chunks):
    context = "\n\n".join(retrieved_chunks)
    prompt= f"""
Answer the question using only the context below.
context:
{context}
Question:
{query}
If the answer is not present in the context, say that it is not available in the document.
"""

    interaction = client.interactions.create(
        model="gemini-3.6-flash",
        input=prompt
    )

    return interaction.output_text

if __name__ == "__main__":
    answer = generate_answer("What is a vector database?")
    print(answer)