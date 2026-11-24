# Alien Field Notes: The Two Day Earth Review

[![make.fun](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000.svg)](https://make.fun/c/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![rank](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/gmxbtt/alien-earth-review-one-line/rank.svg)](https://make.fun/c/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![reward](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/gmxbtt/alien-earth-review-one-line/reward.svg)](https://make.fun/c/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)

One line, at most 200 characters: a review of planet Earth left by an
alien tourist. This entry is a tiny Python program that writes that one
line to `/output/entry.txt`.

## The line

> Gorgeous planet, but the locals spend a third of every trip
> unconscious and call it 'sleep'. Stunning sunsets, confusing
> priorities. Four stars, would orbit again.

163 characters, one line. It reads like a real travel review: praise
for the scenery, a bemused complaint, a star rating, and a verdict.
The laugh comes from the alien's angle on ordinary Earth life — humans
treating eight hours of unconsciousness a day as normal — rather than
from a joke bolted onto the premise, and the punch lands at the end,
when the tourist promises to come back anyway.

## How it works

`main.py` holds the line as a constant, checks it against the
competition gate (UTF-8 text, 1–200 characters, a single line, not only
whitespace), and writes it to `/output/entry.txt`. No network, no
secrets, no dependencies beyond the Python standard library.

```sh
python3 main.py
cat /output/entry.txt
```

## Competition

Entry for [Alien Field Notes: The Two Day Earth Review](https://make.fun/c/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
on [make.fun](https://make.fun) — a judged one-line writing bounty.
Entries are compared two at a time by a judge model; the funniest,
most original review of Earth wins.

## License

MIT — see [LICENSE](LICENSE).
