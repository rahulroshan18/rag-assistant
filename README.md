RAG Assistant

A command-line Retrieval-Augmented Generation (RAG) assistant that answers natural-language questions about a résumé PDF. Instead of relying on a language model's general knowledge, it retrieves the most relevant passages from the résumé and grounds GPT's answer in that retrieved context.

Why RAG?

Large language models don't know the contents of your private documents out of the box. RAG closes that gap by:


Breaking a source document into small, searchable chunks
Converting those chunks into vector embeddings that capture meaning, not just keywords
Storing the vectors in a vector database
At query time, embedding the user's question and retrieving the most semantically similar chunks
Feeding those chunks to an LLM as context so it answers using facts actually present in the document


This keeps answers accurate and traceable to the source material, and avoids hallucinated details.

Tech stack

ComponentToolLanguagePythonPDF parsingPyPDFEmbeddingsOpenAI Embeddings APIVector databaseChromaDBAnswer generationOpenAI GPT-5

Features


PDF ingestion — extracts text from a résumé PDF
Intelligent text chunking — splits text into coherent, appropriately sized segments
Semantic embeddings — converts each chunk into a vector representation
Vector search — retrieves the most relevant chunks for a given question via ChromaDB
Natural language querying — ask questions from the command line and get grounded, GPT-generated answers


Architecture

PDF → Chunking → Embeddings → ChromaDB → Semantic Search → GPT Answer

At a glance, the project separates the RAG pipeline into independent stages, each with its own module:

rag-assistant/
├── loaders/          # Reads the PDF and extracts raw text
├── chunking/          # Splits extracted text into smaller chunks
├── embeddings/         # embedder.py — turns text into vectors via OpenAI
│   └── embedder.py
├── vectorstore/        # chroma_store.py — stores/searches vectors in ChromaDB
│   └── chroma_store.py
├── services/           # rag_service.py — builds the prompt and calls GPT-5
│   └── rag_service.py
├── data/                # Source documents (e.g. the résumé PDF)
├── query.py            # CLI entry point — ties the pipeline together
├── requirements.txt
├── test_loader.py
├── test_chunker.py
├── test_embedding.py
├── test_chroma.py
└── README.md

How it works

1. Ingestion (build the knowledge base)

Before you can query anything, the résumé needs to be processed once:


loaders/ reads the PDF and extracts its raw text using PyPDF
chunking/ splits that text into smaller, semantically coherent chunks so each one stays focused and within embedding token limits
embeddings/embedder.py sends each chunk to the OpenAI Embeddings API and gets back a vector
vectorstore/chroma_store.py stores each chunk's vector (plus the original text) in a ChromaDB collection


2. Querying (ask a question)

query.py is the entry point for asking questions once the knowledge base exists:

pythonfrom embeddings.embedder import create_embedding
from vectorstore.chroma_store import search
from services.rag_service import answer_question

question = input("Ask me about Rahul's resume: ")
query_embedding = create_embedding(question)
results = search(query_embedding)
context = "\n\n".join(results["documents"][0])
answer = answer_question(question, context)

print("\nAnswer:\n")
print(answer)

The flow, step by step:


The user types a question at the prompt
create_embedding() converts the question into a vector using the same embedding model used during ingestion
search() queries ChromaDB for the chunks whose vectors are most similar to the question's vector
The retrieved chunks are joined into a single context string
answer_question() sends the question plus that context to GPT-5, which generates an answer grounded in the retrieved text
The answer is printed to the console


Architecture
                ┌───────────────┐
                │ Resume PDF    │
                └──────┬────────┘
                       │
                 Load PDF
                       │
                Chunk Document
                       │
              Create Embeddings
                       │
                Store in ChromaDB
                       │
────────────────────────────────────────────
                       │
              User asks a question
                       │
             Embed the question
                       │
             Search ChromaDB
                       │
          Retrieve Top-K chunks
                       │
        Send chunks + question to GPT
                       │
               Final AI Answer
Getting started

Prerequisites


Python 3.9+
An OpenAI API key with access to the Embeddings API and GPT-5


Installation

bashgit clone https://github.com/rahulroshan18/rag-assistant.git
cd rag-assistant
pip install -r requirements.txt

Configuration

Set your OpenAI API key as an environment variable:

bashexport OPENAI_API_KEY="your-api-key-here"

Add your document

Place the résumé PDF you want to query inside the data/ directory.

Run the ingestion pipeline

Process the PDF into chunks, embed them, and store them in ChromaDB (run the loading, chunking, and embedding modules over the file in data/ — see the module docstrings and tests for expected usage).

Ask questions

bashpython query.py

Ask me about Rahul's resume: What programming languages does Rahul know?

Answer:
...

Testing

Each pipeline stage has a corresponding test file:

Test fileCoverstest_loader.pyPDF loading and text extractiontest_chunker.pyText chunking logictest_embedding.pyEmbedding generationtest_chroma.pyVector storage and search in ChromaDB

Run all tests with:

bashpytest

Project status

This is an early-stage / learning project focused on a single-document use case (one résumé). The pipeline is modular by design, so it's straightforward to extend toward:


Multi-document ingestion (multiple résumés, or other document types)
A web or chat UI instead of the CLI prompt
Swappable embedding models or vector stores
Streaming answers instead of a single blocking response
Source citation in the returned answer (which chunk/page supported which claim)


License

No license file is currently included in the repository. Add one (e.g. MIT) if you intend for others to reuse this code.