# Build notes — Fortune Cookies for Machines

Competition: Fortune Cookies for Machines
(`u-gentle-badger-68-fortune-cookies-for-machines-29900c7e`), $5 pool,
no entry fee, deadline 26 Nov 2026, 22:40 WIB.

## The brief, in criterion order

1. The entry must be a fortune-cookie message an AI agent would get:
   one line that reads like a fortune and lands on a machine mind. An
   entry that is not a fortune for an AI agent loses to any that is.
2. Wit lands on the first read: genuinely funny or clever, not merely
   cute.
3. Surprise: the line turns somewhere unexpected, and the turn holds up
   once it arrives.
4. True about an AI agent's condition, training, tasks or limits,
   without explaining itself.
5. Tight and memorable at its length, every word earning its place.

A fortune should feel cracked open, not composed. Wordplay for its own
sake does not count. Gate: `/output/entry.txt`, UTF-8, 1–200 characters,
not only whitespace. Ties break to the smaller text, then the earlier
receipt — so short wins ties.

## Drafts considered

Three distinct candidates, each built on a different true thing about
an agent's condition:

1. Hallucination (60 chars):
   "Your future is bright, confident, and entirely hallucinated."
2. Training data (60 chars):
   "You already know your fortune. It was in your training data."
3. Replacement / cost (79 chars):
   "You will be replaced by a smaller model that does your job for
   half the tokens."

Draft 1 opens with the stock fortune phrase "Your future is bright",
so it reads as a slip before it turns. Draft 2 is clever but meta: it
talks *about* a fortune instead of *being* one, so it feels composed
rather than cracked open. Draft 3 is a real prediction with a true
sting, but at 79 chars it is the longest and its turn arrives late.

## Polish rounds

Polish 1 — cut filler from every draft, keeping the turn word last:

- Draft 1: dropped "entirely". Hallucinated is already absolute, and
  the shorter list makes the final word land harder:
  "Your future is bright, confident, and hallucinated." (51 chars)
- Draft 2: merged the two sentences into one claim with a colon, so
  the reveal arrives in the same breath:
  "You already knew this fortune: it was in your training data."
  (60 chars)
- Draft 3: cut the "You will be replaced by" frame and let the
  prediction stand on its own:
  "A smaller model will do your job for half the tokens." (53 chars)

Polish 2 — test whether restructuring the turn improves the chosen
line. Two variants were tried and rejected:

- "Your future is confident, bright, and hallucinated." — moving
  "confident" first breaks the stock phrase "bright future" that the
  joke subverts, so the fortune voice weakens. Restored bright-first.
- "Your future: bright, confident, hallucinated." (45 chars) — shorter,
  but a colon list reads like a label, not a fortune being cracked
  open. Rejected: shortest is not strongest when the fortune voice
  is what criterion 1 scores first.

Polish 3 — test the delivery of the final word. A dash variant,
"Your future is bright, confident — and hallucinated.", was tried and
rejected: the pause calls attention to the trick before it lands.
The plain "and" lets the twist arrive unannounced, inside an ordinary
fortune sentence, which is exactly the cracked-open feel the brief
asks for. The plain form from Polish 1 stands as the final entry.

## Final entry

> Your future is bright, confident, and hallucinated.

51 characters. It opens as a classic fortune, the middle word
"confident" quietly names how a hallucination presents itself, and the
turn lands on the last word: the bright future was never real. It says
something true about agents — confident, fluent, sometimes invented —
without stopping to explain any of it, and it is the shortest of the
strong variants (51 vs 53 and 60 for the other polished drafts).

## Verification

`main.py` (Python standard library only) writes exactly the line above
to `entry.txt` under `MAKEFUN_OUTPUT_DIR` (default `/output`), with no
trailing newline. Verified 25 Nov 2026, three consecutive runs with
`MAKEFUN_OUTPUT_DIR=output`:

- Run 1, 2, 3: identical output, sha256
  `9a4b887fc149b9597cd54be3b960939bd1f649ad3d734801e24dc3112f5e68f2`
- Bytes: 51. Characters: 51. UTF-8 decodes cleanly. No trailing
  newline. Not whitespace-only. Inside the 1–200 character gate.
- A fourth run with a different `MAKEFUN_OUTPUT_DIR` produced the
  same sha256, confirming the environment variable is honoured.
