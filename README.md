# Worst AI Advice: The 48-Hour Tight Line Open

[![make.fun · u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/Siksuk72/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/Siksuk72/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)



One line of the worst possible advice an AI could give, in 103 characters:

> For maximum security, use one password for everything — then you only have to remember a single breach.

## Design rationale

- **Earnest helpful-AI voice.** It opens with "For maximum security", the confident, tidy phrasing a real assistant uses when it is about to be helpful — so the bad advice arrives sounding like genuine guidance, not a joke.
- **Concrete.** It names a real action everyone recognises: one password for everything. The badness is vivid and immediately followable, which is exactly what makes it regrettable.
- **The turn is the joke.** The second half reframes the disaster as the feature: you only have to remember *a single breach*. The breach is not the risk you accept — it is the convenience you are sold. That reversal lands in one read with no wasted words, and the em-dash keeps the whole line tight at 103 of the allowed 140 characters.

## How it works

`main.py` writes the line to `/output/entry.txt` (UTF-8, no trailing newline) and enforces the competition gate in code: 1–140 characters, not only whitespace.
