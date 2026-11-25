#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh (make.fun).

Scores six original one-line roasts of a smart fridge against the judge
brief's five criteria, in the brief's own order (weights 5/4/3/2/1), and
writes the winner to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Judge criteria, most important first:
  1. Roast of a smart fridge (fridge, app, firmware, ice maker).
  2. Punchline lands: a turn or surprise on first read.
  3. Specific to smart fridges, not a generic gadget gag.
  4. Tight wording: every word earns its place (<= 200 chars).
  5. Fresh: avoids the obvious cracks (fridge ordering groceries,
     fridge watching you).

Rejected drafts (documented, not entered):
  - "My fridge ordered milk before I knew I was out - it shops better
    than I do, and judges me for it." REJECTED: the ordering-groceries
    crack is the brief's own named cliche (criterion 5).
  - "My fridge watches me eat at 2 a.m. and logs it like a
    disappointed parent." REJECTED: the watching-you crack is the
    brief's other named cliche (criterion 5).
  - "My smart fridge is smarter than me: it has a degree in
    refrigeration and I have a degree in opening it." REJECTED: the
    joke aims at the owner, not the fridge (criterion 1), and the turn
    is a mild pun, not a real punchline (criterion 2).
"""

import os

# (line, [on_subject, punchline, specific, tight, fresh]) - each 1..5.
CANDIDATES = [
    ("I asked my fridge for ice. It demanded a software update, my "
     "Wi-Fi password, and time to reconsider our relationship.",
     [5, 5, 5, 5, 5]),
    ("My smart fridge updated its firmware overnight and now it judges "
     "my midnight snacks in a language I don't speak.",
     [5, 4, 5, 4, 4]),
    ("My fridge has a camera inside, a touchscreen outside, and the "
     "emotional range of a landlord inspecting the freezer.",
     [5, 4, 4, 4, 4]),
    ("My fridge's ice maker filed a noise complaint against itself, "
     "then emailed me a survey about the experience.",
     [5, 4, 5, 4, 4]),
    ("My smart fridge beeps when the door's been open ten seconds, "
     "like it's timing me stealing my own leftovers.",
     [5, 3, 4, 4, 3]),
    ("My fridge's touchscreen froze mid-update, so now it just shows "
     "a spinning wheel and my shame.",
     [5, 3, 4, 5, 3]),
]

WEIGHTS = [5, 4, 3, 2, 1]


def score(scores):
    """Weighted total; the brief's criteria in order, most important first."""
    return sum(w * s for w, s in zip(WEIGHTS, scores))


def pick():
    """Highest weighted score wins; ties break to the shorter line."""
    ranked = sorted(
        CANDIDATES,
        key=lambda c: (score(c[1]), -len(c[0])),
        reverse=True,
    )
    return ranked[0][0]


def main():
    line = pick()
    # Gate from the brief: UTF-8 text, 1-200 chars, exactly one line.
    assert 1 <= len(line) <= 200, f"line is {len(line)} chars"
    assert "\n" not in line, "line must be a single line"
    line.encode("utf-8")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)
    print(line)
    print(f"({len(line)} chars, score {score(dict((c[0], c[1]) for c in CANDIDATES)[line])})")


if __name__ == "__main__":
    main()
