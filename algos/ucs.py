from models.track import Track
from models.terrain import TerrainType
from helpers.valid_square import is_valid_square

def ucs(grid, track: Track) -> Track:
    # Implement Uniform Cost Search algorithm
    if track.start.position == track.end.position:
        return track

    # Initialize the tracking queue with the start node
    track.open_list = [track.start]
    track.closed_list[track.start.position] = track.start
    
    while track.open_list:
        current_node = track.remove_open(track.open_list[0])

        if current_node.position == track.end.position:
            return track
        
        track.closed_list[current_node.position] = current_node

        # Check neighboring squares
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in directions:
            next_x = current_node.position[0] + dx
            next_y = current_node.position[1] + dy
            
            if not is_valid_square(grid, next_x, next_y):
                continue
            
            if (next_x, next_y) in track.closed_list:
                continue

            child_node = current_node.add_child(TerrainType[grid[next_x][next_y].char].value, (next_x, next_y))
            track.closed_list[(next_x, next_y)] = child_node
            track.add_open_sorted(child_node)