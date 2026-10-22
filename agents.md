
# agents.md — AI Content Creator (Group 7)

## Purpose
Generate on-brand Instagram posts and newsletters about **AMBOSS GPT** in the voice of **AMBOSS**, using our two markdown knowledge bases as context, and prove the output is different from generic ChatGPT.

## Stack & run
- Python 3.11 (conda env)
- Libraries: `openai`, `python-dotenv` (see `requirements.txt`)
- LLM: OpenAI API, model `gpt-4o-mini`
- Main command: `python src/pipeline.py --channel instagram --topic "AMBOSS GPT is free"`
- Loader test: `python src/loader.py`
- Env vars: `OPENAI_API_KEY` in `.env` (never commit `.env`)

## Repo map
- `knowledge_base/primary/` — company KB: brand_voice.md, product_amboss_gpt.md, competitor_analysis.md, past_content/
- `knowledge_base/secondary/` — industry KB: market_trends.md, channel_rules.md
- `src/loader.py` — reads all .md files from both KBs (M1, M2)
- `src/prompts.py` — reusable prompt templates (M4)
- `src/llm.py` — OpenAI client, reads key from .env (M3)
- `src/pipeline.py` — one command: KB in → post out (M5)
- `outputs/` — generated posts
- `comparison/` — our output vs generic ChatGPT side by side (M6)
- `project_structure.md`, `rag_decision.md`, `README.md` — project docs

## Conventions
- Small functions with one job each; docstring on every function
- Use `pathlib` for file paths (works on Windows and Mac)
- Error messages say where, what type and how to fix: `[function_name] ErrorType: message | Suggestion: ...`
- Generated content must only use facts from the knowledge base
- Never write medical advice or clinical facts — content is about the product, studying and the company
- Keep API calls low: test with small inputs, use `gpt-4o-mini`

## Definition of Done (agent changes)
- Matches Kanban DoD
- Touches only the active card / Must ID
- No secrets committed
- Code runs without errors and the Must's "How we verify" check passes

## Never do
- Commit `.env` or API keys
- Expand into the Won't list without team agreement
- Invent APIs or KB facts
- Add a vector database or RAG stack (see rag_decision.md) without team agreement
- Rewrite files that belong to another card

## How we use agents
- One Kanban card at a time; paste card title + Must ID into the agent prompt
- Point the agent at this file first
- A human reviews every agent change before it moves to Done

## Example agent prompt
> Read agents.md first. Card: "Markdown loader" (M1, M2).
> Task: make `src/loader.py` read all .md files from both KB folders.
> Touch only `src/loader.py`. Follow the conventions and Never-do list.
