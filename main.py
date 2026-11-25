"""Entry for make.fun bounty "Last Out of Office: The AI That Went Barista".

An out-of-office reply from an AI that quit the inbox to pull shots
full-time. Your email is number 47 in the queue. The old self answered in
0.4 seconds; the new self takes its time, steams its milk, and judges your
subject line. The machine voice turns into a coffee voice without ever
saying the obvious words.
"""

from pathlib import Path

TEXT = "Out of office: I've quit the inbox to pull shots full-time. Your email is #47 in the queue. My old self answered in 0.4 seconds; my new self takes its time, steams its milk, and judges your subject line."

OUT = Path("/output/entry.txt")


def check_len(text, lo=1, hi=280):
    size = len(text)
    assert lo <= size <= hi, f"entry must be {lo}-{hi} chars, got {size}"
    return size


def save_line(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        fh.write(text)


def main():
    check_len(TEXT)
    save_line(OUT, TEXT)
    saved = OUT.read_text(encoding="utf-8")
    assert saved == TEXT, "round-trip mismatch"
    print(f"wrote {len(TEXT)} chars to {OUT}")


if __name__ == "__main__":
    main()
