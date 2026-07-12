from embeddings.embedder import create_embedding

embedding = create_embedding("Rahul is learning AI.")

print(type(embedding))

print(len(embedding))

print(embedding[:10])