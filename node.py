"""
----------------------------------------
Institute of Business Administration
Spring 2022
----------------------------------------
Introduction to Artificial Intelligence
Class 60766
----------------------------------------
Syed, Danial Haseeb
ERP 12429
----------------------------------------
Term Project:
Pathfinder
----------------------------------------
Class: Node
----------------------------------------
"""
from location import *


class Node:
    """
    A node in a search tree. Contains its `Location` and a pointer to
    its `parent` node.
    
    Note: if a `Location` is arrived at by two paths, then there are
    two nodes with the same `Location`.  This class also keeps track of
    the total path cost, `g(n)`, to reach the node.
    """
    def __init__(self, x, y, parent=None):
        """
        Create a search tree Node, derived from a parent by an action.
        """
        self.location = Location(x,y)
        self.parent = parent

    def neighbour(self, direction: Direction) -> Location:
        """
        Return neighbouring location in the given direction.
        """
        return self.location + direction.value

    def expand(self):
        """Return a list of nodes reachable from this node."""
        expansion = []

        for direction in Direction:
            location = self.neighbour(direction)
            x, y = location.x, location.y
            child = Node(x, y, self)
            if not (child.location.isOutside() or child.location.isObstacle()):
                expansion.append(child)
        
        return expansion
    
    def path(self):
        """
        Return a list of nodes forming the path from the root to this
        node.
        """
        node = self
        pathBack = []

        while node:
            pathBack.append(node)
            node = node.parent

        return list(reversed(pathBack))

    def __eq__(self, other):
        return isinstance(other, Node) and (self.location == other.location)

    def __hash__(self):
        return hash(self.location)

    def __repr__(self):
        return self.location.__repr__()
    

def g(n):
    """
    Return the cost of the path from the root to the given node.
    """
    if n.parent is None:
        return 0
    return g(n.parent) + 1