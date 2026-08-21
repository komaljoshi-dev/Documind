import gradio as gr

from src.indexer import create_document_index
from src.rag import ask_question

pdf_paths = [
    "data/sample.pdf",
    "data/another.pdf"
]

index, chunks = create_document_index(pdf_paths)

def respond(query):
    answer, sources = ask_question(query,index,chunks)

    sources_text="\n".join(
        f"{source} - Page {page}"
        for source, page in sources
    )
    return answer, sources_text

with gr.Blocks() as demo:
    gr.Markdown("# Documind")
    question = gr.Textbox(
        label = "Ask a question",
        placeholder= "Ask something about your documents..."
    )

    answer = gr.Markdown()
    sources = gr.Markdown()
    button = gr.Button("Ask")

    button.click(
        fn = respond,
        inputs = question,
        outputs=[answer, sources]
    )

demo.launch()