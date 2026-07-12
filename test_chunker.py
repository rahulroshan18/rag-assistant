from loaders.pdf_loader import load_pdf
from chunking.text_chunker import chunk_text

text = load_pdf("data/Rahul_Roshan_Resume.pdf")

chunks = chunk_text(text)

print(f"Total Chunks: {len(chunks)}")

for i, chunk in enumerate(chunks):
    print("=" * 60)
    print(f"Chunk {i+1}")
    print("=" * 60)
    print(chunk[:250])
    print()