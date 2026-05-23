from models.track import Track
from helpers.map_loader import load_map
from helpers.visualizer import visualize
from algos.bfs import bfs
from algos.ucs import ucs
from algos.a_star_1 import a_star_1
from algos.a_star_2 import a_star_2

# Maps
# grid, start, end = load_map("./maps/map1_stupid.txt")
# grid, start, end = load_map("./maps/map2_simple.txt")
grid, start, end = load_map("./maps/map3_complex.txt")

track = Track(start, end)

# Algorithm runs
# final_track: Track = bfs(grid, track)
final_track: Track = ucs(grid, track)
# final_track: Track = gbfs(grid, track)
# final_track: Track = a_star_1(grid, track)
# final_track: Track = a_star_2(grid, track)

visualize(grid, final_track)