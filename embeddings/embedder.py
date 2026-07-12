from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def create_embedding(text: str):
    """
    Create an embedding for the given text using OpenAI's API.
    """
    try:
        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=text
        )
        return response.data[0].embedding
    except Exception as e:
        raise Exception(f"Error creating embedding: {e}")