from models.track import Track
from models.terrain import TerrainType
from helpers.valid_square import is_valid_square

def a_star_2(grid, track: Track) -> Track:
    # Implement A* Search with Euclidean distance heuristic
    if track.start.position == track.end.position:
        return track

    g_scores = {track.start.position: 0}  # local g tracking
    
    track.open_list = [track.start]
    track.start.total_value = 0  # f = g + h = 0 + h_start
    
    while track.open_list:
        current_node = track.remove_open(track.open_list[0])

        track.closed_list[current_node.position] = current_node
        current_g = g_scores[current_node.position]

        if current_node.position == track.end.position:
            return track

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in directions:
            next_x = current_node.position[0] + dx
            next_y = current_node.position[1] + dy

            if not is_valid_square(grid, next_x, next_y):
                continue
            
            if (next_x, next_y) in track.closed_list:
                continue

            terrain_cost = TerrainType[grid[next_x][next_y].char].value
            tentative_g = current_g + terrain_cost
            
            # Skip if we've already found an equal or better path to this neighbor
            if (next_x, next_y) in g_scores and g_scores[(next_x, next_y)] <= tentative_g:
                continue
            
            g_scores[(next_x, next_y)] = tentative_g
            heuristic = ((next_x - track.end.position[0])**2 + (next_y - track.end.position[1])**2) ** 0.5
            
            child_node = current_node.add_child(terrain_cost, (next_x, next_y))
            child_node.total_value = tentative_g + heuristic  # f = g + h
            track.add_open_sorted(child_node)
    return track