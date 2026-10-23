# AMBOSS AI Content Creator

An educational prototype for generating and revising AMBOSS-style marketing content with a Gradio interface or an interactive command-line workflow. The application uses the project's Markdown knowledge bases as context and OpenAI to generate drafts.

> **Independent project notice:** This is a bootcamp project for educational purposes. It is not affiliated with, endorsed by, sponsored by, or officially connected to AMBOSS. Generated content is a draft and should be reviewed before publication.

## Features

- Generate content for Instagram, newsletters, LinkedIn, and blogs.
- Choose an output language: English, German, Spanish, French, or Hindi.
- Select a content strategy: brand, industry, or hybrid.
- Set the target audience, primary and secondary keywords, and tone of voice.
- Revise a draft using reviewer feedback in the Gradio interface.
- Save generated content as Markdown files through the command-line workflow.
- Use primary AMBOSS materials and secondary industry materials as prompt context.

The application injects the Markdown knowledge-base content directly into prompts; it does not use a vector database or retrieval-augmented generation (RAG).

## Requirements

- Python 3.11
- An OpenAI API key

Install the runtime dependencies from the repository root:

```bash
python -m pip install -r requirements.txt
```

## Setup

1. Clone the repository and open a terminal in its root directory.
2. Create a `.env` file in the root directory:

   ```dotenv
   OPENAI_API_KEY=your_openai_api_key
   ```

   The application uses `gpt-4o-mini` by default. To select a different model, optionally add `LLM_MODEL=your-model-name` to `.env`.

3. Keep `.env` private. It is ignored by Git; never commit API keys.

## Run the web interface

From the repository root, run:

```bash
python -m src.gradio_interface
```

Open the local URL printed in the terminal. Enter a content request, configure the options, and select **Generate Content**. To improve the draft, enter reviewer feedback and select **Revise Content**. Review and copy the resulting draft before publishing; drafts generated in this interface are not automatically saved to `outputs/`.

## Run the command-line workflow

From the repository root, run:

```bash
python -m src.main
```

Follow the prompts to enter the channel, request, keywords, language, strategy, audience, and tone. The generated Markdown draft is saved in `outputs/`.

## Knowledge bases

Markdown files are loaded from both directories and used as generation context:

- `knowledge_base/primary/` — brand guidelines, product information, and past content.
- `knowledge_base/secondary/` — competitor analysis and market trends.

Keep product and brand claims grounded in the primary knowledge base. Secondary materials provide industry context, not authority for AMBOSS-specific claims. The prompt rules prohibit unsupported claims and medical advice.

## Project structure

```text
knowledge_base/
  primary/                 # AMBOSS brand and product context
  secondary/               # Industry and competitor context
src/
  content_pipeline.py      # Loads context, builds prompts, generates and saves drafts
  document_processor.py    # Reads and splits Markdown knowledge-base files
  gradio_interface.py      # Web interface for generation and revision
  knowledge_base.py        # Organizes knowledge-base context
  llm_integration.py       # OpenAI API integration
  main.py                  # Interactive command-line workflow
  prompt_templates.py      # Channel-specific generation and revision prompts
outputs/                   # Markdown drafts saved by the command-line workflow
```

## Notes

- OpenAI API usage may incur costs and is subject to the provider's limits.
- Generated content can be inaccurate or incomplete. A qualified human should review factual, medical, brand, and legal claims before publication.
- The app is a content-generation prototype; it does not publish content to social platforms.

For the project's requirements and architecture decisions, see [project_structure.md](./project_structure.md) and [rag_decision.md](./rag_decision.md).
