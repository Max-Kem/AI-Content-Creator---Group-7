from src.content_pipeline import run_pipeline


def main():
    """Run the AMBOSS AI Content Creator."""

    channel = input("Channel (instagram/newsletter): ")
    request = input("Content request: ")
    primary_keyword = input("Primary keyword: ")
    secondary_keyword = input("Secondary keyword: ")

    output_path = run_pipeline(
        channel=channel,
        request=request,
        primary_keyword=primary_keyword,
        secondary_keyword=secondary_keyword
    )

    print(f"\nContent successfully saved to: {output_path}")


if __name__ == "__main__":
    main()


