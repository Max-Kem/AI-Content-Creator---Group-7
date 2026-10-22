from src.document_processor import load_pieces
from src.knowledge_base import build_knowledge_context
from src.prompt_templates import generate_content_prompt
from src.llm_integration import generate_content

def load_knowledge_context() -> dict:
    """
    Load the AMBOSS knowledge bases and prepare
    primary and secondary context for content generation.
    """

    # File 1: Read and process Markdown documents
    pieces = load_pieces()

    # File 2: Organize primary and secondary knowledge
    contexts = build_knowledge_context(pieces)

    return contexts

def build_content_prompt(
    channel: str,
    request: str,
    primary_keyword: str,
    secondary_keyword: str
) -> str:
    """Build a content prompt using the AMBOSS knowledge bases."""

    # Load knowledge base context
    contexts = load_knowledge_context()

    # File 3: Generate the channel-specific prompt
    prompt = generate_content_prompt(
        channel=channel,
        request=request,
        primary=primary_keyword,
        secondary=secondary_keyword,
        contexts=contexts
    )

    return prompt


def generate_draft(
    channel: str,
    request: str,
    primary_keyword: str,
    secondary_keyword: str
) -> str:
    """Generate AMBOSS content using the knowledge base and OpenAI API."""

    # Files 1–3: Build the prompt with knowledge base context
    prompt = build_content_prompt(
        channel=channel,
        request=request,
        primary_keyword=primary_keyword,
        secondary_keyword=secondary_keyword
    )

    # File 4: Generate content with the LLM
    system_prompt = (
        "You are an AI content creator for AMBOSS. "
        "Follow the provided brand guidelines and channel rules. "
        "Use the knowledge base as your factual source. "
        "Do not invent medical or product-related claims."
    )

    result = generate_content(
        system_prompt=system_prompt,
        user_prompt=prompt
    )

    return result

def save_draft(content: str, channel: str) -> str:
    """Save generated content as a Markdown file."""

    from pathlib import Path
    from datetime import datetime

    # Create output directory if it doesn't exist
    output_dir = Path(__file__).resolve().parent.parent / "outputs"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Create a unique filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    filename = f"{channel.lower()}_{timestamp}.md"

    # Save generated content
    output_path = output_dir / filename
    output_path.write_text(content, encoding="utf-8")

    return str(output_path)


def run_pipeline(
    channel: str,
    request: str,
    primary_keyword: str,
    secondary_keyword: str
) -> str:
    """Run the complete content generation and saving pipeline."""

    # Step 1: Generate content using the LLM
    content = generate_draft(
        channel=channel,
        request=request,
        primary_keyword=primary_keyword,
        secondary_keyword=secondary_keyword
    )

    # Step 2: Save the generated content
    output_path = save_draft(content, channel)

    return output_path
