from models.cell import Cell
from models.node import Node

def load_map(filepath):
    grid = []
    start = None
    end = None

    with open(filepath) as f:
        for r, line in enumerate(f):
            row_cells = []
            
            for c, ch in enumerate(line.strip()):
                if ch == 'S':
                    start = Node((r, c))
                    cell = Cell(r, c, 'S')
                elif ch == 'E':
                    end = Node((r, c))
                    cell = Cell(r, c, 'E')
                else:
                    cell = Cell(r, c, ch)
                
                row_cells.append(cell)
            
            grid.append(row_cells)
            
    return grid, start, end