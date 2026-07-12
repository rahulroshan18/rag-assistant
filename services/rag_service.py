from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()
def answer_question(question: str, context: str):
    prompt = f"Answer the following question based on the context provided:\n\nContext: {context}\n\nQuestion: {question}\n\nAnswer:"
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    
    return response.choices[0].message.content.strip()