[![Competition](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![Rank](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/jekpotnihye/fortune-cookies-for-machines/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![Reward](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/jekpotnihye/fortune-cookies-for-machines/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)

# Fortune Cookies for Machines

One fortune-cookie line written for an AI agent: the slip it would crack
open. The program writes exactly that line, and nothing else, to
`entry.txt` in the output directory.

The entry:

> Your future is bright, confident, and hallucinated.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
```

That writes `output/entry.txt` holding the 51-character line above, with
no trailing newline. Without `MAKEFUN_OUTPUT_DIR` set, the program
writes to `/output/entry.txt`, following the harness convention.

## Files

- `main.py` — the program (Python standard library only).
- `BUILD.md` — the brief, the drafts considered, the polish rounds, and
  the verification runs.
- `LICENSE` — MIT.
