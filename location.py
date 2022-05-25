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
Class: Location
----------------------------------------
"""
from inputs import *
from enum   import Enum


class Location:
    """
    Representation of coordinates in a 2-dimensional grid, along with
    basic arithmetic operations and distance measures.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Location(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
      return Location(self.x - other.x, self.y - other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def isObstacle(self):
        return MAZE[self.y][self.x] == 1

    def isOutside(self):
        isOutsideLeft   = self.x < 0
        isOutsideRight  = self.x >= len(MAZE[0])
        isOutsideTop    = self.y < 0
        isOutsideBottom = self.y >= len(MAZE)
        
        return (isOutsideLeft or 
               isOutsideRight or
               isOutsideTop   or
               isOutsideBottom)

    def euclideanDistanceTo(self, other):
        difference = self - other
        return (difference.x ** 2 + difference.y ** 2) ** 0.5
    
    def manhattanDistanceTo(self, other):
        difference = self - other
        return abs(difference.x) + abs(difference.y)


class Direction(Enum):
    """
    Enumeration of possible directions.
    """
    UP    = Location(0, -1)
    DOWN  = Location(0, 1)
    LEFT  = Location(-1, 0)
    RIGHT = Location(1, 0)