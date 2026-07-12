from embeddings.embedder import create_embedding
from vectorstore.chroma_store import search
from services.rag_service import answer_question

question = input("Ask me about Rahul's resume: ")

query_embedding = create_embedding(question)

results = search(query_embedding)

context = "\n\n".join(results["documents"][0])

answer = answer_question(question, context)

print("\nAnswer:\n")
print(answer)