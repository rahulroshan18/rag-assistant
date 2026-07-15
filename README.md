# 📚 Enterprise RAG Assistant

An enterprise-style **Retrieval-Augmented Generation (RAG)** application built using **Python**, **OpenAI Embeddings**, and **ChromaDB**. This project demonstrates how AI systems can retrieve relevant information from custom documents using semantic search before generating responses.

Instead of relying solely on an LLM's training data, the assistant retrieves the most relevant document context, improving response accuracy and reducing hallucinations.

---

# 📌 Project Overview

Large Language Models have limited knowledge of private or enterprise documents. Retrieval-Augmented Generation (RAG) solves this problem by combining document retrieval with AI-generated responses.

This project implements a complete RAG pipeline that:

- Loads PDF documents
- Extracts text
- Splits documents into semantic chunks
- Generates vector embeddings
- Stores embeddings in ChromaDB
- Performs semantic similarity search
- Retrieves the most relevant context for answering questions

---

# 🏗 Architecture

```
               PDF Document
                     │
                     ▼
              PDF Loader
                     │
                     ▼
            Text Extraction
                     │
                     ▼
              Text Chunking
                     │
                     ▼
         OpenAI Embeddings
                     │
                     ▼
          ChromaDB Vector Store
                     │
                     ▼
              User Question
                     │
                     ▼
        Generate Query Embedding
                     │
                     ▼
          Semantic Search
                     │
                     ▼
       Retrieve Best Chunks
                     │
                     ▼
             AI Response
```

---

# 🚀 Features

- 📄 PDF document loading
- 📝 Automatic text extraction
- ✂ Intelligent text chunking
- 🧠 OpenAI embedding generation
- 🗂 ChromaDB vector database integration
- 🔍 Semantic similarity search
- 📑 Context retrieval using embeddings
- ⚡ Reduced token usage through targeted retrieval
- 🏗 Modular and extensible project architecture

---

# 🧠 Key AI Concepts

## PDF Loader

Extracts text from PDF documents using PyPDF.

---

## Text Chunking

Large documents are divided into smaller chunks to preserve context while enabling efficient retrieval.

Benefits:

- Better semantic matching
- Lower embedding costs
- Improved retrieval accuracy
- Reduced LLM token consumption

---

## Embeddings

Each text chunk is converted into a numerical vector using OpenAI Embeddings.

Embeddings capture semantic meaning instead of relying on exact keyword matches.

---

## ChromaDB

Stores vector embeddings for fast similarity search.

Instead of scanning the entire document, the system retrieves only the most relevant chunks.

---

## Semantic Search

When a user submits a question:

1. The query is converted into an embedding.
2. ChromaDB compares it against stored document embeddings.
3. The closest matching chunks are retrieved.
4. The retrieved context is supplied to the LLM.

This approach significantly improves answer relevance compared to traditional keyword search.

---

# 🔄 Workflow

1. Load PDF document.
2. Extract text.
3. Split text into semantic chunks.
4. Generate embeddings for each chunk.
5. Store embeddings in ChromaDB.
6. Receive user query.
7. Generate query embedding.
8. Perform semantic similarity search.
9. Retrieve relevant context.
10. Generate AI response.

---

# 📂 Project Structure

```
rag-assistant/
│
├── chunking/
│   └── text_chunker.py
│
├── embeddings/
│   └── embedding_generator.py
│
├── loaders/
│   └── pdf_loader.py
│
├── vectorstore/
│   └── chroma_store.py
│
├── data/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
└── tests/
```

---

# ⚙ Technologies Used

- Python 3.13
- OpenAI Embeddings
- ChromaDB
- PyPDF
- python-dotenv

---

# 🛠 Installation

Clone the repository:

```bash
git clone https://github.com/rahulroshan18/rag-assistant.git

cd rag-assistant
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

macOS/Linux

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file:

```text
OPENAI_API_KEY=your_api_key_here
```

---

# ▶ Running the Project

Run the application:

```bash
python3 query.py
```

The application will:

- Load the PDF
- Generate embeddings
- Store vectors
- Perform semantic search
- Retrieve relevant document context

---

# 💡 AI Concepts Demonstrated

This project demonstrates:

- Retrieval-Augmented Generation (RAG)
- Embedding Models
- Semantic Search
- Vector Databases
- Document Chunking
- Context Retrieval
- Enterprise Knowledge Retrieval
- Modular AI Architecture

---

# 📈 Future Enhancements

Planned improvements include:

- Conversational RAG
- Memory
- Hybrid Search (Keyword + Vector)
- Multi-document Support
- Metadata Filtering
- FastAPI REST API
- Web Interface
- Streaming Responses
- Citation Support
- Docker Deployment

---

# 🎯 Learning Outcomes

This project provides practical experience in:

- Designing RAG pipelines
- Working with vector databases
- Optimizing document chunking strategies
- Understanding semantic similarity
- Building enterprise knowledge assistants
- Improving LLM accuracy through retrieval

---

# 📸 Sample Execution

```
Loading PDF...

Chunking document...

Generating embeddings...

Saving vectors to ChromaDB...

User Query:
What experience does Rahul have in AI?

Retrieved Context:
Top 3 matching document chunks...

Generating Response...
```

---

# 👨‍💻 Author

**Rahul Roshan**

Enterprise Architect | AI Engineer | Principal System Architect

GitHub:
https://github.com/rahulroshan18

---

# ⭐ Support

If you found this project useful, consider giving the repository a ⭐ and feel free to share feedback or suggestions.