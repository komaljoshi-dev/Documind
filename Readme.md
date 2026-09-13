# DocuMind

DocuMind is a document question-answering application built with **Retrieval-Augmented Generation (RAG)**.

Upload one or more PDF documents, ask questions about their contents, and get answers generated from the most relevant sections of those documents. DocuMind uses semantic search with **Sentence Transformers and FAISS** to retrieve relevant context before passing it to **Google Gemini** for answer generation.

## Features

* Upload one or multiple PDF documents
* Extract text from PDF pages
* Split documents into overlapping chunks
* Generate semantic embeddings using Sentence Transformers
* Search document content using FAISS
* Generate context-grounded answers using Google Gemini
* Display the source document and page number for retrieved information
* Simple web interface built with Gradio
* Support for multiple documents in a single session

## How It Works

DocuMind follows a Retrieval-Augmented Generation pipeline:

```text
PDF Documents
      │
      ▼
 Text Extraction
      │
      ▼
  Text Chunking
      │
      ▼
Sentence Transformer
   Embeddings
      │
      ▼
   FAISS Index
      │
      │
      ▼
 User Question
      │
      ▼
 Query Embedding
      │
      ▼
 Similarity Search
      │
      ▼
Relevant Chunks
      │
      ▼
    Gemini
      │
      ▼
 Answer + Sources
```

### 1. Document Processing

Uploaded PDFs are processed using `pypdf`. Text is extracted page by page, while the page number and source document are preserved.

The extracted text is then divided into smaller overlapping chunks to make semantic retrieval more effective.

### 2. Embeddings

Each document chunk is converted into a vector representation using the `all-MiniLM-L6-v2` Sentence Transformer model.

This allows the application to search for content based on semantic similarity rather than relying only on exact keyword matches.

### 3. Vector Search

The generated embeddings are stored in a **FAISS `IndexFlatL2`** index.

When a user asks a question, the question is converted into an embedding and compared against the document embeddings. The most relevant chunks are retrieved.

### 4. Answer Generation

The retrieved chunks are passed to Google's Gemini API as context.

The model is instructed to answer the question using only the retrieved document content. If the required information cannot be found in the retrieved context, the application asks the model to indicate that the information is not available in the document.

### 5. Sources

Each retrieved chunk retains its original document name and page number.

DocuMind displays these sources below the generated answer so that users can identify where the retrieved information came from.

## Tech Stack

| Technology            | Purpose                         |
| --------------------- | ------------------------------- |
| Python                | Application and RAG pipeline    |
| Gradio                | Web interface                   |
| PyPDF                 | PDF text extraction             |
| Sentence Transformers | Text embeddings                 |
| FAISS                 | Vector similarity search        |
| Google Gemini         | Answer generation               |
| python-dotenv         | Environment variable management |

## Project Structure

```text
DocuMind/
│
├── app.py                  # Gradio web application
├── requirements.txt        # Python dependencies
├── .gitignore
│
└── src/
    ├── chunking.py         # Text chunking
    ├── embeddings.py       # Embedding generation
    ├── generator.py        # Gemini answer generation
    ├── indexer.py          # FAISS index creation
    ├── ingest.py           # PDF text extraction
    ├── rag.py              # RAG pipeline
    ├── retrieval.py        # Similarity search
    └── test_rag.py         # Local testing script
```

`test_rag.py` is used for local testing and is intentionally excluded from version control.

## Getting Started

### Prerequisites

* Python 3.10 or later
* A Google Gemini API key
* Git

### 1. Clone the repository

```bash
git clone https://github.com/komaljoshi-dev/Documind.git
cd Documind
```

### 2. Create a virtual environment

**Windows PowerShell**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Gemini API key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

The `.env` file is included in `.gitignore` and should never be committed to the repository.

### 5. Run the application

```bash
python app.py
```

Gradio will start the application locally.

## Using DocuMind

1. Open the DocuMind application.
2. Upload one or more PDF documents.
3. Click **Process documents**.
4. Wait for the documents to be processed.
5. Enter a question about the uploaded documents.
6. Click **Ask** or press Enter.
7. Read the generated answer.
8. Check the **Sources** section to see the document and page associated with the retrieved information.

## Example

After uploading a document containing information about machine learning, you could ask:

```text
What machine learning models were used?
```

DocuMind retrieves the most relevant sections of the uploaded document and provides them to Gemini as context for generating the answer.

## Retrieval Configuration

The current implementation uses:

* **Embedding model:** `all-MiniLM-L6-v2`
* **Chunk size:** 150 words
* **Chunk overlap:** 30 words
* **Retrieved chunks:** Top 3 results
* **FAISS index:** `IndexFlatL2`
* **Distance threshold:** 1.8

These parameters can be adjusted in the source code depending on document size and retrieval performance.

## Limitations

* PDF text extraction currently depends on machine-readable text.
* Scanned or image-only PDFs are not currently supported.
* Document indexes are stored in application memory.
* The index is rebuilt when documents are processed and is not persisted between application restarts.
* Retrieval quality depends on chunk size, embedding quality, and the retrieval threshold.
* Answers are based on the information retrieved from the uploaded documents.
* Gemini API usage is subject to the limits and pricing of the configured Google API account.

## Future Improvements

* Add OCR support for scanned and image-based PDFs
* Persist document indexes between application sessions
* Add conversation history for follow-up questions
* Improve source highlighting and citation display
* Experiment with reranking and improved retrieval strategies

## Author

**Komal**

Built to explore Retrieval-Augmented Generation, semantic search, embeddings, vector indexing, and LLM application development.
