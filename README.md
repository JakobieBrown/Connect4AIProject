# Connect Four

A two-player game with support for human and AI-controlled players.

---

## Requirements

- **Python** 3.13.1
- **matplotlib** — `pip install matplotlib`
- **pygame** — `pip install pygame`

---

## Running the Game

The program has two modes: **game mode** and **test mode**.

### Game Mode

Run a game with any combination of human and AI players.

```bash
python main.py --player1 --player2 --fps FPS --depth DEPTH
```

By default, both players are human-controlled. Pass `--player1` and/or `--player2` to hand control of that player over to the AI agent.

**Examples:**

```bash
# Two human players
python main.py

# Player 1 is AI, Player 2 is human
python main.py --player1

# Both players are AI
python main.py --player1 --player2

# Both players are AI, running at 30 FPS with search depth 4
python main.py --player1 --player2 --fps 30 --depth 4
```

### Test Mode

Run automated tests of the AI agent playing against itself.
The tests will collect metrics from full games at every depth up to the supplied depth.
```bash
python main.py --test --depth DEPTH
```

**Example:**

```bash
# Run tests with agent search depth of 5
python main.py --test --depth 5
```

---

## Command-Line Arguments

| Argument | Description |
|---|---|
| `--player1` | Player 1 is controlled by the AI agent (default: human) |
| `--player2` | Player 2 is controlled by the AI agent (default: human) |
| `--fps FPS` | Set the frame rate of the game (e.g. `--fps 60`) |
| `--depth DEPTH` | Set the search depth for the AI agent and/or tests (e.g. `--depth 4`) |
| `--test` | Run the test module (AI vs AI) instead of launching a game |
