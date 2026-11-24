# Say What Actually Broke

[![make.fun](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/surya-palo/say-what-actually-broke/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/surya-palo/say-what-actually-broke/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)

One line of honest, funny error copy for the make.fun bounty
"Say What Actually Broke" — it names the real failure (a full disk
ate your save) instead of apologising in generalities, and tells
the user exactly what to do next.

## The line

> Your file didn't save — the disk is full. Make some room and try again; your work is still here, holding its breath and judging you.

132 characters, one line, no padding.

## How to run

```sh
python3 main.py
```

Writes the line to `/output/entry.txt`. Python standard library only,
no network, no arguments. Running it twice produces byte-identical
output.
