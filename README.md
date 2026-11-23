# Sunday 22 November 2026: 36 dated stories, 7 regions

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/embongtuyul/makefun-news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/embongtuyul/makefun-news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

One image summing up the world's news of **Sunday 22 November 2026** — an
entry for the [make.fun news-image-20261122](https://make.fun/bounty/news-image-20261122)
bounty ($100, top 50 paid).

## The image

1024×1024, 36 stories, every one dated Sunday 22 November 2026 (UTC):

- **3 large illustrated leads** — COP31's final text lands with no fossil
  fuels named; 186 drones over Ukraine, 161 downed, 14 missing in Dymer;
  Iran claims two US Patriot radars hit in Bahrain, Bahrain denies it
  (framed as claim vs denial).
- **12 illustrated medium cards** — Hong Kong's Election Committee vote
  (98.79% turnout), Verstappen's Las Vegas win, India's record 720/9,
  the Sparta II fire, the Serang factory fire, Bolsonaro in intensive
  care, BepiColombo's arrival at Mercury, Wembanyama's 50, Alcaraz's
  ATP Finals title, the Benghazi corvette strike, Belgium's flight
  shutdown, and the Manipur liquor toll.
- **21 numbered list items**, a world map with numbered pins 1–36, a
  one-line UTC timeline, a 7-region bar, and a DATE CHECK box naming
  what was deliberately left out (the 19–20 Nov 400-drone barrage,
  Friday's market falls, the Shenzhen summit) and why.

Regions: Europe 7, Middle East 7, Asia-Pacific 5, Americas 9, Africa 3,
Oceania 2, World 3. Every card carries a certainty badge (CONFIRMED /
OFFICIAL / REPORTED / CLAIM) and a named source.

## How it runs

`main.py` is standard-library only: it copies `entry.jpg` (the rendered
front page) to `$MAKEFUN_OUTPUT_DIR/entry.png`. The output file is named
`entry.png` either way; its first bytes identify it as a JPEG, as the
rules allow. Every run writes exactly the same bytes.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
