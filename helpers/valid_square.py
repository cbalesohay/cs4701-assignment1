from models.terrain import TerrainType

def is_valid_square(grid, x, y) -> bool:
    # Check if coordinates are within the grid boundaries
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
        return False
    # Avoid water
    elif grid[x][y].char == TerrainType.W.name:
        return False
    else:
        return grid[x][y]