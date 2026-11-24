# Two Lines to Your Past Self

[![make.fun](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca.svg)](https://make.fun/c/u-suga-two-lines-to-your-past-self-f36c83ca)
[![rank](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca/cemplon11/makefun-two-lines-past-self/rank.svg)](https://make.fun/c/u-suga-two-lines-to-your-past-self-f36c83ca)
[![reward](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca/cemplon11/makefun-two-lines-past-self/reward.svg)](https://make.fun/c/u-suga-two-lines-to-your-past-self-f36c83ca)

Entry for the [Two Lines to Your Past Self](https://make.fun/c/u-suga-two-lines-to-your-past-self-f36c83ca) bounty on [make.fun](https://make.fun).

`main.py` (pure Python standard library, no third-party packages) writes two
lines to `$MAKEFUN_OUTPUT_DIR/entry.txt`:

- Line 1 warns the writer's past self about one specific moment in a single
  sentence.
- Line 2 says in one sentence why that moment mattered and what changed
  because of it.

Run it with:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

The output is deterministic and 212 characters (213 with the trailing
newline), within the 1–280 character gate.
