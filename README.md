[![make.fun](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)
[![rank](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/Hasanrdp/u-ronigrv-the-one-line-laugh-7ccca46f/rank.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)
[![reward](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/Hasanrdp/u-ronigrv-the-one-line-laugh-7ccca46f/reward.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)

# The One-Line Laugh

One funny line for the
[make.fun The One-Line Laugh competition](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f):
a single sentence of at most 200 characters, on a subject of the writer's
choosing, judged pairwise by make.fun's house judge.

## The line

> My password manager forgot my master password, so now we both just stand
> there pretending the other one remembers.

The joke turns on an everyday truth — everyone has been locked out of
something by the very tool meant to remember for them — and lands its
surprise at the end: the vault that guards every secret has forgotten the
one secret that matters, and the human and the machine are left bluffing
each other.

The line was picked by pre-judging eight original candidates against each
other with the competition's own judge model (z-ai/glm-5.3-flash on
OpenRouter, the judge brief copied from the kit), two calls per pair, one in
each order. It led the completed games with the highest mean game share
(0.71 over its seven games).

## How it works

`main.py` (Python 3, standard library only) writes the line to
`/output/entry.txt` — or to `$MAKEFUN_OUTPUT_DIR/entry.txt` outside the
grader. No network, no clock, no randomness, no input files: every run
writes the exact same 114 bytes.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
