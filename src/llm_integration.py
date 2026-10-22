import os

from dotenv import load_dotenv
from openai import (
    OpenAI,
    AuthenticationError,
    APIConnectionError,
    RateLimitError,
    APIStatusError,
)


def generate_content(system_prompt: str, user_prompt: str) -> str:
    """
    Send system and user prompts to the OpenAI API
    and return the generated content as text.

    Args:
        system_prompt: Instructions and rules for the LLM.
        user_prompt: User request and knowledge base context.

    Returns:
        Generated content as a string.
    """

    # Load API configuration
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("LLM_MODEL", "gpt-4o-mini")

    # Validate configuration and prompts
    if not api_key:
        raise ValueError("OPENAI_API_KEY is missing from .env.")

    if not system_prompt.strip() or not user_prompt.strip():
        raise ValueError("System and user prompts must not be empty.")

    try:
        # Initialize OpenAI client
        client = OpenAI(
            api_key=api_key,
            timeout=30.0,
            max_retries=0
        )

        # Send prompts to OpenAI
        response = client.responses.create(
            model=model,
            instructions=system_prompt,
            input=user_prompt,
            max_output_tokens=600
        )

        # Extract generated text
        generated_text = response.output_text.strip()

        if not generated_text:
            raise RuntimeError("The LLM returned an empty response.")

        return generated_text

    except AuthenticationError as error:
        raise RuntimeError(
            "OpenAI authentication failed. Check your API key."
        ) from error

    except RateLimitError as error:
        raise RuntimeError(
            "OpenAI rate limit or API quota reached."
        ) from error

    except APIConnectionError as error:
        raise RuntimeError(
            "Could not connect to the OpenAI API."
        ) from error

    except APIStatusError as error:
        raise RuntimeError(
            f"OpenAI API error: HTTP {error.status_code}"
        ) from error
