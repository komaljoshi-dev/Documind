from .retrieval import retrieve
from .generator import generate_answer

def ask_question(query,index,chunks):

    results = retrieve(query, index, chunks)

    if not results:
       return "I couldn't find the answer in the documents.", []
    
    
    retrieved_chunks = [result["chunk"]["text"] for result in results]
    answer = generate_answer(query, retrieved_chunks)
    
    sources = sorted(
    set(
        (result["chunk"]["source"] ,result["chunk"]["page"])
        for result in results
        )
    )
    return answer, sources