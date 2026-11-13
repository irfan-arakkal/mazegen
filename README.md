*This activity has been created as part of the 42 curriculum by iarakkal, <teammate_login>.*

# A-Maze-ing

## Description

A-Maze-ing is a maze generator written in Python. It reads a configuration
file, generates a random (but reproducible) maze, writes it to an output file
using a hexadecimal wall encoding, and shows it in the terminal.

Two kinds of mazes can be generated:

- **Perfect maze** (`PERFECT=True`): exactly one path between the entry and
  the exit, with no loops.
- **Pac-Man board** (`PERFECT=False`): every corridor is reachable, the four
  corners and the centre are open, there are several independent routes
  (loops), and dead-ends are rare.

Every maze contains a visible "42" drawn with fully closed cells, when the
maze is big enough.

The maze generation logic lives in a reusable package, `mazegen`, that can be
installed with pip and imported in other projects.

## Instructions

### Requirements

- Python 3.10 or later
- `make`

### Installation

```bash
git clone https://github.com/irfan-arakkal/mazegen.git
cd mazegen
python3 -m venv .venv
source .venv/bin/activate
make install
```

### Run

```bash
make run
```

This runs `python3 a_maze_ing.py config.txt`. To use another configuration
file:

```bash
python3 a_maze_ing.py my_config.txt
# or
make run CONFIG=my_config.txt
```

### Other Makefile rules

| Rule | What it does |
|---|---|
| `make install` | Install the project dependencies |
| `make run` | Run the program with the default config |
| `make debug` | Run the program in the Python debugger (pdb) |
| `make clean` | Remove caches (`__pycache__`, `.mypy_cache`) |
| `make lint` | Check style (flake8) and types (mypy) |
| `make lint-strict` | Same, with `mypy --strict` |

## Configuration file

The configuration file contains one `KEY=VALUE` pair per line. Lines starting
with `#` are comments and are ignored, as are empty lines.

| Key | Required | Description | Example |
|---|---|---|---|
| `WIDTH` | yes | Maze width, in cells (positive integer) | `WIDTH=20` |
| `HEIGHT` | yes | Maze height, in cells (positive integer) | `HEIGHT=15` |
| `ENTRY` | yes | Entry coordinates `x,y` (0-based, inside the maze) | `ENTRY=0,0` |
| `EXIT` | yes | Exit coordinates `x,y` (inside the maze, different from `ENTRY`) | `EXIT=19,14` |
| `OUTPUT_FILE` | yes | Name of the output file | `OUTPUT_FILE=maze.txt` |
| `PERFECT` | yes | `True` for a perfect maze, `False` for a Pac-Man board | `PERFECT=True` |
| `SEED` | no | Random seed; the same seed always gives the same maze | `SEED=42` |

Default `config.txt`:

```
# Default A-Maze-ing configuration
WIDTH=20
HEIGHT=15
ENTRY=0,0
EXIT=19,14
OUTPUT_FILE=maze.txt
PERFECT=True
SEED=42
```

If the file is missing or invalid (missing key, wrong value, entry or exit
outside the maze, etc.), the program prints a clear error message and stops
without crashing.

## Output file format

Each cell is written as one hexadecimal digit. Each bit tells whether a wall
is closed (1) or open (0):

| Bit | Wall |
|---|---|
| 0 (LSB) | North |
| 1 | East |
| 2 | South |
| 3 | West |

Cells are written row by row, one row per line. After an empty line, three
more lines follow: the entry coordinates, the exit coordinates, and the
shortest path from entry to exit using the letters `N`, `E`, `S`, `W`.

## Maze generation algorithm

TODO: describe the chosen algorithm (e.g. recursive backtracker) and how the
Pac-Man mode is built.

### Why this algorithm

TODO: explain the choice.

## Reusable module

TODO: how to install the `mazegen` package (`.whl`), create a
`MazeGenerator`, pass custom parameters (size, seed), access the generated
grid and get a solution, with a short code example.

## Team and project management

### Roles

- **iarakkal**: configuration parsing and error handling, output file,
  terminal display and user interactions, Makefile and linting.
- **<teammate_login>**: maze generation (`MazeGenerator`), "42" pattern,
  perfect and Pac-Man modes, shortest path, pip package and licence.

### Planning

TODO: planned schedule and how it evolved.

### What worked well and what could be improved

TODO.

### Tools used

Git and GitHub, VS Code, flake8, mypy, make.

## Resources

- [Python documentation](https://docs.python.org/3/)
- [Maze generation algorithm (Wikipedia)](https://en.wikipedia.org/wiki/Maze_generation_algorithm)
- [Breadth-first search (Wikipedia)](https://en.wikipedia.org/wiki/Breadth-first_search)
- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)
- [mypy documentation](https://mypy.readthedocs.io/)
- [Python Packaging User Guide](https://packaging.python.org/)

### Use of AI

AI (Claude) was used to:

- plan the project and split the work between team members;
- explain Python concepts (dataclasses, exceptions, file reading);
- review code and explain errors;
- write a first draft of this README.

All code was written, tested and understood by the team members.
