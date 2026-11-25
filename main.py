import os
from pathlib import Path

# One-line comedy entry for make.fun's One-Liner Marathon.
# Final line: the strongest of three candidates drafted for this entry,
# picked against the judge's brief (works as a joke in one line, the
# surprise turn lands on the first read, tightest wording, deadpan
# voice, and it holds up on a second read).
LINE = "I bought a book called How to Spot a Scam six months ago, and it still hasn't arrived."


def main() -> None:
    if not 1 <= len(LINE) <= 280:
        raise ValueError(f"entry must be 1-280 characters, got {len(LINE)}")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(LINE, encoding="utf-8")
    written = target.read_text(encoding="utf-8")
    if written != LINE:
        raise RuntimeError("entry.txt on disk does not match the line")
    print(f"wrote {len(written)} characters to {target}")


if __name__ == "__main__":
    main()
