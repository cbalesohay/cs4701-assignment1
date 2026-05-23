from collections import deque
from models.track import Track
from models.node import Node
from models.terrain import TerrainType
from helpers.valid_square import is_valid_square

def bfs(grid, track: Track) -> Track:
    if track.start.position == track.end.position:
        return track

    # Initialize the tracking queue with the start node
    track.open_list_queue = deque([track.start])
    track.closed_list[track.start.position] = track.start
    
    while track.open_list_queue:
        current_node = track.open_list_queue.popleft()

        if current_node.position == track.end.position:
            return track
        
        track.closed_list[current_node.position] = current_node

        # Check neighboring squares
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in directions:
            next_x = current_node.position[0] + dx
            next_y = current_node.position[1] + dy

            if is_valid_square(grid, next_x, next_y) and (next_x, next_y) not in track.closed_list:
                child_node = current_node.add_child(TerrainType[grid[next_x][next_y].char].value, (next_x, next_y))
                track.closed_list[(next_x, next_y)] = child_node
                track.open_list_queue.append(child_node)