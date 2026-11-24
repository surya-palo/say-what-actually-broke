# Build log — Say What Actually Broke

## What was built
- `main.py` (Python stdlib only): writes one original error line to
  `/output/entry.txt`. No network, no arguments, no randomness.
- The line was written from scratch in this session, then genuinely
  improved in a second, separately committed edit:
  - v1 (127 chars): "Your file didn't save — the disk is full. Free up some
    space and try again; your work is still in this tab, holding its breath."
  - v2 (132 chars): "Your file didn't save — the disk is full. Make some room
    and try again; your work is still here, holding its breath and judging you."
  - The second edit tightened the call to action ("Make some room" vs
    "Free up some space") and added the quotable closing twist
    ("and judging you"), the part a reader repeats to a colleague —
    the judge's core criterion.
- `README.md` with the 3 live make.fun badges, the line, and run instructions.
- `LICENSE` (MIT + SPDX-License-Identifier: MIT).
- `.makefun/owner.json` (57 bytes, no trailing newline).

## The final line
> Your file didn't save — the disk is full. Make some room and try again; your work is still here, holding its breath and judging you.

## Verification (2026-11-24, local run)
- Character count: 132 (limit 200) — PASS
- Single line, no newline in file — PASS
- Non-blank UTF-8 text — PASS
- Determinism: ran `python3 main.py` twice; both runs byte-identical — PASS
- sha256 of `/output/entry.txt`:
  `eec91bd6c14d0ad0b3fb7a972cb9fd9c7d663730bd5d24b36ac71821e27aa192`
- File bytes: 134 (132 chars; the em dash is 3 bytes in UTF-8)
- `.makefun/owner.json`: 57 bytes, no trailing newline — PASS
- Git history: 2 commits for the line (draft + improvement), plus
  README/LICENSE/owner.json commit.

## Not done here (parent's job)
- No `makefun bundle` / `makefun check` run, no GitHub repo created,
  no submission. No wallet, API key, or credential touched.
