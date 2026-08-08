# Tic-Tac-Toe (with an AI you can't beat)

A simple tic-tac-toe game I built to mess around with the minimax algorithm.
There's a console version in Python and a browser version you can actually
deploy and share.

The AI never loses. Best you can do is force a draw - that's just how
minimax works, it plays perfectly every time.

## Play it

**In the browser:** open `index.html`, or check the live link if it's up on
GitHub Pages.

**In the terminal:**
```bash
python3 tic_tac_toe.py
```
Pick X or O, then just type the row and column (0-2) when it's your turn.

## Running the tests

```bash
pip install pytest
pytest tests/
```

## Files

```
project1/
├── index.html              -> browser version, HTML/CSS/JS
├── tic_tac_toe.py           -> console version
├── tests/test_tic_tac_toe.py
├── README.md
├── LICENSE
└── .gitignore
```

## How the AI actually works

It's minimax - basically the AI plays out every possible way the rest of
the game could go, assuming you also play your best move every time, and
picks whatever move guarantees it the best result. Tic-tac-toe has a tiny
enough search space that this runs instantly, no optimizations needed.

## License

MIT, see LICENSE file.
