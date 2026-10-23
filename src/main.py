from src.content_pipeline import run_pipeline


def main():
    """Run the AMBOSS AI Content Creator."""

    channel = input("Channel (instagram/newsletter/linkedin/blog): ")
    request = input("Content request: ")
    primary_keyword = input("Primary keyword: ")
    secondary_keyword = input("Secondary keyword: ")
    language = input(
        "Language (english/german/spanish/french/hindi) [english]: "
    ).strip().lower() or "english"
    strategy = input(
        "Content strategy (brand/industry/hybrid) [hybrid]: "
    ).strip().lower() or "hybrid"
    audience = input(
        "Target audience [medical students and healthcare professionals]: "
    ).strip() or "medical students and healthcare professionals"
    tone = input(
        "Tone of voice (professional/educational/engaging/empathetic) [professional]: "
    ).strip().lower() or "professional"

    output_path = run_pipeline(
        channel=channel,
        request=request,
        primary_keyword=primary_keyword,
        secondary_keyword=secondary_keyword,
        language=language,
        strategy=strategy,
        audience=audience,
        tone=tone
    )

    print(f"\nContent successfully saved to: {output_path}")


if __name__ == "__main__":
    main()


