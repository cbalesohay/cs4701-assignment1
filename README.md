# CS4701 Assignment 1 — Pathfinding

Implements five pathfinding algorithms on a terrain grid:
- Breadth-First Search (BFS)
- Uniform Cost Search (UCS)
- Greedy Best-First Search (GBFS)
- A* Search with one admissible heuristic (A*1)
- A* Search with a second, different heuristic (A*2)

## Setup

```bash
python3 -m venv venv
source venv/bin/activate    # Mac/Linux
pip install -r requirements.txt
```

## Run

```bash
python3 app.py
```

To switch algorithms or maps, edit `app.py` and uncomment the desired lines.