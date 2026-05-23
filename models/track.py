from typing import List
from collections import deque
from models.node import Node

class Track:
    def __init__(self, start: Node = None, end: Node = None):
        self.open_list: List[Node] = []
        self.open_list_queue: deque[Node] = deque()
        self.closed_list: dict[tuple[int, int], Node] = {}
        self.start: Node = start
        self.end: Node = end
        
    def add_open(self, node: Node):
        self.open_list.append(node)
        
    def add_open_sorted(self, node: Node):
        self.open_list.append(node)
        # (lowest first)
        self.open_list.sort(key=lambda n: n.total_value)
        
    def remove_open(self, node: Node) -> Node:
        self.open_list.remove(node)
        return node
        
    def add_closed(self, node: Node):
        self.closed_list[node.position] = node