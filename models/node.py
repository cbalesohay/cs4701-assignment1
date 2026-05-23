from typing import List, Tuple

class Node:
    def __init__ (self, position: Tuple[int, int] = None, total_value: int = 0, parent = None):
        self.position: Tuple[int, int] = position
        self.total_value: int = total_value
        self.parent: Node = parent
        self.children: List[Node] = []
        
    def add_child(self, path_value: int, position: Tuple[int, int]) -> Node:
        new_child = Node(position, path_value + self.total_value, self)
        self.children.append(new_child)
        return new_child