def format_retrieved_chunks(chunks) -> str:
    """
    Combine retrieved documents into a single formatted string.
    """
    if not chunks:
        return ""
    
    result = "\n\n".join(doc.page_content for doc in chunks)
    return f"Relevant reference materials:\n\n{result}"
