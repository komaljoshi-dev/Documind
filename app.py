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

    return f"Successfully processed {len(files)} PDF(s) and {len(chunks)} chunks.You can ask Questions now."


def respond(query):
    if index is None:
        return "Please upload and process your documents first.",""
    if not query.strip():
        return "Please enter a question.", ""
    
    answer, sources = ask_question(query,index,chunks)

    sources_text = "\n".join(
        f"{source} - Page {page}"
        for source, page in sources
    )

    return answer, sources_text

css = """

.gradio-container {
    max-width: 1000px !important;
    margin: 0 auto !important;
    padding: 28px 16px 48px !important;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
}

#header {
    text-align: center;
    margin-bottom: 24px;
}

#header h1 {
    font-size: 32px;
    font-weight: 700;
    margin: 0 0 6px 0;
}

#header p {
    font-size: 15px;
    margin: 0;
    opacity: 0.7;
}

.dm-card {
    border-radius: 12px !important;
    padding: 20px !important;
    gap: 12px !important;
    margin-bottom: 20px !important;
    border: 1px solid var(--border-color-primary) !important;
    background: var(--background-fill-primary) !important;
}

.dm-card-title {
    font-size: 16px !important;
    font-weight: 600 !important;
    margin: 0 0 4px 0 !important;
}

#process-btn,
#ask-btn {
    width: auto !important;
    min-width: 130px !important;
    border-radius: 8px !important;
    font-weight: 500 !important;
}

#ask-btn {
    align-self: stretch !important;
    height: auto !important;
}

#answer,
#sources {
    border-radius: 12px !important;
    padding: 18px 20px !important;
    min-height: 60px;
    border: 1px solid var(--border-color-primary) !important;
    background: var(--background-fill-primary) !important;
}

#answer p,
#sources p,
#sources li {
    font-size: 15px;
    line-height: 1.6;
}

.dm-section-label {
    font-size: 15px !important;
    font-weight: 600 !important;
    margin: 4px 0 8px 0 !important;
    opacity: 0.85;
}

#status {
    font-size: 14px !important;
    min-height: 0;
}

/* ---------- Footer ---------- */
#footer {
    text-align: center;
    font-size: 13px;
    margin-top: 28px;
    opacity: 0.55;
}
"""


with gr.Blocks(
    title="DocuMind",
    theme=gr.themes.Soft(primary_hue="blue", neutral_hue="slate"),
    css=css,
) as demo:

    # ---------- Header ----------
    gr.Markdown(
        """
        # DocuMind
        Ask questions about your documents using AI-powered retrieval.
        """,
        elem_id="header",
    )

    # ---------- Upload ----------
    with gr.Column(elem_classes="dm-card"):
        gr.Markdown("Upload documents", elem_classes="dm-card-title")

        files = gr.File(
            label="PDF documents",
            file_count="multiple",
            file_types=[".pdf"],
            height=200,
        )

        with gr.Row():
            process_button = gr.Button(
                "Process documents",
                variant="primary",
                elem_id="process-btn",
            )

        status = gr.Markdown(elem_id="status")

    # ---------- Question ----------
    with gr.Column(elem_classes="dm-card"):
        gr.Markdown("Ask a question", elem_classes="dm-card-title")

        with gr.Row():
            question = gr.Textbox(
                label="",
                placeholder="e.g. What machine learning models were used?",
                lines=2,
                show_label=False,
                container=False,
                scale=5,
            )
            ask_button = gr.Button(
                "Ask",
                variant="primary",
                elem_id="ask-btn",
                scale=1,
            )

    # ---------- Answer ----------
    gr.Markdown("Answer", elem_classes="dm-section-label")
    answer = gr.Markdown(elem_id="answer")

    # ---------- Sources ----------
    gr.Markdown("Sources", elem_classes="dm-section-label")
    sources = gr.Markdown(elem_id="sources")

    # ---------- Footer ----------
    gr.Markdown(
        "DocuMind · FAISS · Sentence Transformers · Gemini",
        elem_id="footer",
    )

    # ---------- Events ----------
    process_button.click(
        fn=process_documents,
        inputs=files,
        outputs=status,
    )

    ask_button.click(
        fn=respond,
        inputs=question,
        outputs=[answer, sources],
    )

    question.submit(
        fn=respond,
        inputs=question,
        outputs=[answer, sources],
    )

demo.launch(share=True)