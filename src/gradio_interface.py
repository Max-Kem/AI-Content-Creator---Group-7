import gradio as gr
from src.content_pipeline import (
    generate_draft,
    build_content_prompt,
    revise_draft
)

def generate_with_prompt(
    channel,
    request,
    primary_keyword,
    secondary_keyword,
    language,
    strategy,
    audience,
    tone
):
    """Generate content and return the draft with its original prompt."""

    original_prompt = build_content_prompt(
        channel=channel,
        request=request,
        primary_keyword=primary_keyword,
        secondary_keyword=secondary_keyword,
        language=language,
        strategy=strategy,
        audience=audience,
        tone=tone
    )

    content = generate_draft(
        channel=channel,
        request=request,
        primary_keyword=primary_keyword,
        secondary_keyword=secondary_keyword,
        language=language,
        strategy=strategy,
        audience=audience,
        tone=tone
    )

    return content, original_prompt

with gr.Blocks(title="AMBOSS AI Content Creator") as demo:
    gr.Markdown("# AMBOSS AI Content Creator")
    gr.Markdown(
        "Generate, review, and revise content using AMBOSS knowledge bases."
    )
    channel = gr.Dropdown(
        choices=["instagram", "newsletter", "linkedin", "blog"],
        value="linkedin",
        label="Content Channel",
        info="Select the platform for your content.",
        interactive=True
    )
    request = gr.Textbox(
        label="Content Request",
        placeholder="e.g., Introduce AMBOSS GPT and highlight its benefits for medical students.",
        lines=3,
        info="Describe the content you want the AI to generate.",
        interactive=True
    )
    
    with gr.Row():
        primary_keyword = gr.Textbox(
            label="Primary Keyword",
            placeholder="e.g., AMBOSS GPT",
            info="Enter the main keyword to emphasize in the generated content.",
            interactive=True
        )
        secondary_keyword = gr.Textbox(
            label="Secondary Keyword",
            placeholder="e.g., medical education",
            info="Enter a supporting keyword to provide additional context.",
            interactive=True
        )

    
    with gr.Row():
        language = gr.Dropdown(
            choices=["english", "german", "spanish", "french", "hindi"],
            value="english",
            label="Output Language",
            info="Select the language for the generated content.",
            interactive=True
        )
        strategy = gr.Dropdown(
            choices=["brand", "industry", "hybrid"],
            value="hybrid",
            label="Content Strategy",
            info="Choose how the AI should use the AMBOSS and industry knowledge bases.",
            interactive=True
        )

    with gr.Row():
        audience = gr.Textbox(
            label="Target Audience",
            placeholder="e.g., Medical students, physicians, or healthcare educators",
            value="medical students and healthcare professionals",
            info="Specify the audience the AI should address.",
            interactive=True
        )
        tone = gr.Dropdown(
            choices=["professional", "educational", "engaging", "empathetic"],
            value="professional",
            label="Tone of Voice",
            info="Select the communication style for the generated content.",
            interactive=True
        )

    generate_button = gr.Button(
        value="Generate Content",
        variant="primary"
    )
    draft = gr.Textbox(
        label="Generated Content",
        placeholder="Your AI-generated content will appear here...",
        lines=12,
        info="Review and manually edit the generated draft before publishing.",
        interactive=True,
        buttons=["copy"]
    )
    feedback = gr.Textbox(
        label="Reviewer Feedback",
        placeholder="e.g., Make the introduction more engaging, shorten the text, and emphasize the benefits for medical students.",
        lines=4,
        info="Describe what the AI should improve in the current draft.",
        interactive=True
    )
    revise_button = gr.Button(
        value="Revise Content",
        variant="secondary"
    )
    original_prompt_state = gr.State(value="")
    generate_button.click(
        fn=generate_with_prompt,
        inputs=[
            channel,
            request,
            primary_keyword,
            secondary_keyword,
            language,
            strategy,
            audience,
            tone
        ],
        outputs=[draft, original_prompt_state]
    )
    revise_button.click(
        fn=revise_draft,
        inputs=[
            original_prompt_state,
            draft,
            feedback
        ],
        outputs=draft
    )


if __name__ == "__main__":
    demo.launch(
        theme=gr.themes.Origin(
            primary_hue="teal",
            secondary_hue="cyan",
            neutral_hue="slate"
        ).set(
            body_background_fill="#F0F4F6",
            block_background_fill="#E5EDF0",
            input_background_fill="#F2F6F7"
        )
    )

