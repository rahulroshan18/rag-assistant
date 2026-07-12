from loaders.pdf_loader import load_pdf
from chunking.text_chunker import chunk_text
from embeddings.embedder import create_embedding
from vectorstore.chroma_store import add_chunks, search

print("Loading PDF...")
text = load_pdf("data/Rahul_Roshan_Resume.pdf")

print("Chunking...")
chunks = chunk_text(text)

print(f"Chunks: {len(chunks)}")

print("Generating embeddings...")
embeddings = [create_embedding(chunk) for chunk in chunks]

print("Saving to ChromaDB...")
add_chunks(chunks, embeddings)

print("Searching...")

query = "What experience does Rahul have in AI?"

query_embedding = create_embedding(query)

results = search(query_embedding)

print(results["documents"])