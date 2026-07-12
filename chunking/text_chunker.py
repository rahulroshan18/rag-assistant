def chunk_text(text: str, chunk_size: int = 500):
    """
    Split text into chunks of approximately chunk_size words.
    Preserve paragraph boundaries where possible.
    """
    paragraphs = text.split("\n\n")
    chunks = []
    current_chunk = ""

    for paragraph in paragraphs:
        if len(current_chunk.split()) + len(paragraph.split()) <= chunk_size:
            current_chunk += paragraph + "\n\n"
        else:
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = paragraph + "\n\n"

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks