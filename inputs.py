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
User Inputs
----------------------------------------
"""


"""
Input the maze as a 2-dimensional array of integers.
The value of each integer represents the type of the cell.
0: Empty cell
1: Obstacle
"""
       # 0 1 2 3 4 5
MAZE = [[0,1,0,0,0,1], # 0
        [0,0,0,1,1,1], # 1
        [1,0,0,0,0,1], # 2
        [1,1,1,0,0,0], # 3
        [0,0,0,0,0,0], # 4
        [1,1,0,0,0,0]] # 5

"""Input the start and end locations."""
start = (0, 0)
goal  = (5, 5)

"""Input depth limit for depth-limited search."""
depthLimit = 5


"""Other visualisation elements."""
# Colours
red     = '#a31f34'
gray    = '#8a8b8c'
blue    = '#1f76a3'
cyan    = '#1fa38e'
green   = '#1fa34c'
yellow  = '#d9bf36'
magenta = '#a31f76'

startColour = red
goalColour  = green

currentNodeColour = yellow

frontierColour = cyan
exploredColour = blue
solutionColour = magenta


# Runtimes
slow   = 2
normal = 1
fast   = 0.5