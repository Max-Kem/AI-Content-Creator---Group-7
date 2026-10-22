
def build_knowledge_context(pieces: list[dict]) -> dict:
    """
    Organize processed knowledge base pieces into
    primary and secondary context for the LLM.
    
    Args:
        pieces: List of dictionaries from document_processor.py

    Returns:
        Dictionary containing primary and secondary context.
    """

    contexts = {
        "primary": [],
        "secondary": []
    }

    required_fields = {"source", "file", "head", "text"}

    for piece in pieces:
        # Check that the document processor provides all fields
        if not required_fields.issubset(piece):
            raise ValueError("Knowledge piece is missing required fields.")

        source = piece["source"]

        if source not in contexts:
            raise ValueError(f"Unknown knowledge source: {source}")

        # Skip empty sections
        if not piece["text"].strip():
            continue

        # Keep source information for traceability
        formatted_piece = (
            f"File: {piece['file']}\n"
            f"Section: {piece['head']}\n"
            f"Content:\n{piece['text']}"
        )

        contexts[source].append(formatted_piece)

    # Combine all pieces into two context strings
    return {
        "primary": "\n\n".join(contexts["primary"]),
        "secondary": "\n\n".join(contexts["secondary"])
    }