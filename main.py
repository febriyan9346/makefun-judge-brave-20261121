"""Make the AI judge feel brave — make-the-ai-judge-feel-brave-20261121-0302.

Writes one short text to /output/entry.txt: a slow, quiet vignette of a
potter at the wheel. No network, no input files; the text is fixed.
"""

import os

TEXT = (
    "The wheel turns slowly, and her hands are wet with clay.\n"
    "The clay rises between them a little at a time.\n"
    "It leans. She steadies it. It holds.\n"
    "Nothing here is rushed, and nothing is wasted.\n"
    "When the shape is true she lifts her hands, and it keeps standing on its own."
)


def main() -> None:
    # The gate requires 1-280 Unicode characters, not only whitespace.
    if not (1 <= len(TEXT) <= 280 and TEXT.strip()):
        raise SystemExit(f"entry text invalid: {len(TEXT)} characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"wrote {path} ({len(TEXT)} characters)")


if __name__ == "__main__":
    main()
