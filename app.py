import gradio as gr

from src.indexer import create_document_index
from src.rag import ask_question

index = None
chunks = None

def process_documents(files):
    global index, chunks

    if not files:
        return "Please upload at least one PDF."

    pdf_paths = [file.name for file in files]

    index,chunks = create_document_index(pdf_paths)

    return f"Successfully processed {len(files)} PDF(s) and {len(chunks)} chunks."


def respond(query):
    if index is None:
        return "Please upload and process your documents first.",""
    
    answer, sources = ask_question(query,index,chunks)

    sources_text = "\n".join(
        f"{source} - Page {page}"
        for source, page in sources
    )

    return answer, sources_text


with gr.Blocks() as demo:

    gr.Markdown("# Documind")
    gr.Markdown("Upload your documents and ask questions about them.")

    files = gr.File(
        label = "Upload PDF documents",
        file_count="multiple",
        file_types=[".pdf"]
    )

    process_button = gr.Button("Process Documents")
    status = gr.Markdown()

    question = gr.Textbox(
        label = "Ask a question",
        placeholder= "Ask something about your documents..."
    )

    ask_button = gr.Button("Ask")

    answer = gr.Markdown()
    sources = gr.Markdown()

    process_button.click(
        fn = process_documents,
        inputs = files,
        outputs = status
    )

    ask_button.click(
    fn = respond,
    inputs = question,
    outputs = [answer, sources]
    )

demo.launch(share=True)