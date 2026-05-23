import numpy as np
from models.terrain import TerrainType
from models.cell import Cell
from models.node import Node

# def load_map(filepath):
#     grid = [Cell]
#     start = None
#     end = None

#     with open(filepath) as f:
#         for r, line in enumerate(f):
#             cell = None
#             for c, ch in enumerate(line.strip()):
#                 if ch == 'S':
#                     start = (r, c)
#                     cell = Cell(r, c, '')
#                 elif ch == 'E':
#                     end = (r, c)
#                     cell = Cell(r, c, '')
#                 else:
#                     cell = Cell(r, c, TerrainType[ch].value[0])
#             grid.append(cell)
#     return grid, start, end

def load_map(filepath):
    grid = []  # 1. Start with a completely empty list
    start = None
    end = None

    with open(filepath) as f:
        for r, line in enumerate(f):
            row_cells = []  # 2. Track cells just for this specific row
            
            for c, ch in enumerate(line.strip()):
                if ch == 'S':
                    start = Node((r, c), 0)
                    cell = Cell(r, c, 'S')  # Pass 'S' or your preferred start char
                elif ch == 'E':
                    end = Node((r, c), 0)
                    cell = Cell(r, c, 'E')  # Pass 'E' or your preferred end char
                else:
                    cell = Cell(r, c, ch)
                
                row_cells.append(cell)  # 3. Add cell to the current row
            
            grid.append(row_cells)  # 4. Add the finished row to the main grid
            
    return grid, start, end