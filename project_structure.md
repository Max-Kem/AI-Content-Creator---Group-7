# Project Structure – AMBOSS AI Content Creator

## 1. Project Identity

- **Project name:** Your AMBOSS Content Creator
- **Primary project type:** R&D
- **Defined goal (1 sentence):** Researching the possibility of automating the company (AMBOSS) content creator, via an easy UI for marketing teams.
- **Start / end:** Day 1 morning → Day 2 presentation
- **Why this is a project (tick at least 4):**
  - [X] Defined goal
  - [X] Limited resources
  - [X] Interdisciplinary
  - [X] Responsibility for results
  - [X] Complex
  - [X] Defined start/end

## 2. Objectives (Quality / Time / Cost)

**Overall objective:** Build an AI content generator that turns AMBOSS open data into on-brand Instagram posts and Newsletters content about AMBOSS GPT, and prove with a side-by-side comparison that it sounds like AMBOSS and not like generic AI.

| Constraint | Our objective |
|---|---|
| Quality | Every post sounds like AMBOSS, uses only facts from our knowledge base, and is clearly different from a generic AI post in a side-by-side comparison. |
| Time | Hard deadline: final presentation on Day 3. |
| Cost | Use a low-cost model (`gpt-4o-mini`) and stay under $5 in total API spend for the whole project. Real API calls only when needed; tests use fake data, and each run is limited to a few posts. |

## 3. Stakeholder Analysis (Quadrants I–IV)

| Role | Interest (H/L) | Influence (H/L) | Quadrant | Engagement in this project |
|---|---|---|---|---|
| AMBOSS Marketing & Content Team | H | H | I | Manage closely: define content requirements, brand voice, and quality expectations. |
| AMBOSS Management / Project Sponsor | H | H | I | Manage closely: define business goals, approve project scope, and evaluate the final product. |
| Project Team (AI Developers) | H | H | I | Manage closely: develop, test, and deliver the AI Content Creator System. |
| AMBOSS Medical Editorial Team | H | H | I | Manage closely: ensure medical accuracy, scientific credibility, and content reliability. |
| AMBOSS Legal & Data Protection Team | L | H | II | Keep satisfied: ensure compliance with data protection, copyright, and applicable regulations. |
| Regional Marketing Teams | H | L | III | Keep informed: provide feedback on localization, regional trends, and target markets. |
| Medical Students & Healthcare Professionals | H | L | III | Keep informed: gather feedback on content relevance, clarity, and usefulness. |
| Other AMBOSS Departments | L | L | IV | Monitor: communicate relevant developments and assess potential future needs. |

### Quadrant Definitions

- **Quadrant I – High Interest / High Influence:** Manage Closely
- **Quadrant II – Low Interest / High Influence:** Keep Satisfied
- **Quadrant III – High Interest / Low Influence:** Keep Informed
- **Quadrant IV – Low Interest / Low Influence:** Monitor

## 4. Requirements → Implementation

### Must-Have Requirements

| ID | Must requirement | Maps to (file / module) | How we verify |
|---|---|---|---|
| M1 | Ingest primary KB Markdown | `src/…` + `knowledge_base/primary/` | Merged in main repository. |
| M2 | Ingest secondary KB Markdown | `src/…` + `knowledge_base/secondary/` | Merged in main repository. |
| M3 | Call LLM with KB context | `src/llm_integration.py`, `src/content_pipeline.py` | Generate an AMBOSS post and verify that its statements are supported by the KB and that its tone follows the brand guidelines. |
| M4 | Reusable prompt templates (≥2) | `src/prompt_templates.py` | Successfully generate different post types (e.g., medical education and product announcements) using the same templates with different inputs. |
| M5 | End-to-end pipeline command | `src/content_pipeline.py`, `main.py` | Execute one command that loads both KBs, processes the user request, generates a post, and saves the output. |
| M6 | Uniqueness evidence vs ChatGPT | `evaluation/uniqueness_comparison.md` | Generate posts for the same request using generic ChatGPT and our system. Compare brand voice, factual accuracy, specificity, and relevance side by side. |
| M7 | RAG decision documented | `rag_decision.md` | Document the chosen approach and justify it using at least 3 criteria (e.g., KB size, retrieval quality, implementation complexity). |
| M8 | Project structured + agents guided | `project_structure.md`, `agents.md` | Verify that all required sections are completed, responsibilities and modules are clearly defined, and agent instructions are followed during development. |

### Won't Have This Sprint

| Won't | Why deferred |
|---|---|
| Automated publishing to LinkedIn, Instagram, and X | The MVP focuses on generating and saving high-quality content. Direct platform integrations require additional API access, authentication, and approval workflows. |
| Automated real-time market trend monitoring | The MVP uses curated Markdown knowledge bases. Live monitoring would require additional APIs, data processing, and ongoing information validation. |
| Automated feedback-based content optimization | A continuous improvement system would require historical engagement data and additional evaluation logic. For the MVP, content quality will be evaluated through a structured side-by-side comparison. |

### MVP Success Criteria

The MVP is considered successful when:

1. Both the primary and secondary knowledge bases are successfully loaded.
2. At least two reusable prompt templates are functional.
3. The system generates an English AMBOSS social media post using the provided knowledge.
4. The complete content generation process can be executed with a single command.
5. The generated output is saved and accessible.
6. A side-by-side comparison demonstrates specific differences between generic ChatGPT content and our knowledge-based AMBOSS content generator.
7. All mandatory project documentation is completed.

## 5. WBS (2 Levels) → Trello

1. **Structure & board**
   - 1.1 Write `project_structure.md`
   - 1.2 Create Trello lists + WIP + DoD
   - 1.3 Write `agents.md`
   - 1.4 Create cards from this WBS
2. **Knowledge bases**
   - 2.1 Primary Markdown set
   - 2.2 Secondary Markdown set
3. **Ingest & context**
   - 3.1 Markdown loader
   - 3.2 Context → prompts (or retrieval if RAG)
4. **Generate & differentiate**
   - 4.1 LLM client + `.env`
   - 4.2 Prompt templates (≥2)
   - 4.3 End-to-end pipeline command
   - 4.4 Uniqueness comparison artifact
5. **Close**
   - 5.1 Finalize `rag_decision.md` (+ structure §7)
   - 5.2 README + demo prep
   - 5.3 Day 1 / Day 2 board screenshots

## 6. Risks (Exactly 3)

| Risk | P (L/M/H) | I (L/M/H) | Strategy | Concrete action |
|---|---|---|---|---|
| Insufficient or low-quality knowledge base data | M | H | Mitigation | Validate collected AMBOSS data, identify missing information early, and prioritize reliable sources. |
| Technical integration issues with the LLM API and content pipeline | M | H | Reduction | Test modules individually, implement error handling, and establish a working MVP early. |
| Delays caused by limited development time and task dependencies | H | H | Avoidance | Prioritize mandatory requirements, assign clear responsibilities, and defer optional features until the MVP is completed. |

### Why These Three?

These risks directly threaten our project's success:

1. **Data availability:** Without sufficient brand and industry knowledge, we cannot build an effective content generator.
2. **Technical functionality:** If the components do not work together, we cannot deliver a functioning MVP.
3. **Time constraints:** With only two days and three team members, delays could prevent us from completing mandatory deliverables.

## 7. RAG Decision

The AMBOSS Marketing and Content Team requires accurate, brand-consistent content that reflects the company's tone of voice and medical expertise. Our Must-Have requirements (M1–M3) require both knowledge bases to be loaded and used as context, but do not require a retrieval system. Since our knowledge bases are relatively small and consist of structured Markdown files, we can inject the relevant content directly into the LLM prompt without implementing RAG. This approach reduces technical complexity, development time, and integration risks while meeting our MVP requirements. **Decision: We will use direct context injection instead of RAG and revisit this decision when the knowledge bases grow beyond the model's practical context limits or selective information retrieval becomes necessary.**

**See also:** [`rag_decision.md`](rag_decision.md).
