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
Helper Variables and Functions
----------------------------------------
"""
from node  import *
from manim import *


# Initialise the start and goal nodes
startNode = Node(start[0], start[1])
goalNode  = Node(goal[0], goal[1])


# Maze Dimensions
height = len(MAZE)
width  = len(MAZE[0])


# Sizes
fontSize = 35
nodeSize = 4 / height
axisSize = nodeSize * fontSize
logoSize = axisSize / fontSize / 2


# Names
ROVER = [
         'Ingenuity',       # [0] A*
         'Perseverance',    # [1] Greedy Best-First
         'InSight',         # [2] Iterative Deepening
         'Curiosity',       # [3] Depth-Limited
         'Phoenix',         # [4] Depth-First
         'Opportunity',     # [5] Uniform-Cost
         'Spirit',          # [6] Breadth-First
         'Viking'           # [7] Best-First
        ]          

ALGORITHM = [
             r'\(A^*\) Search',             # [0] Ingenuity
             'Greedy Best-First Search',    # [1] Perseverance
             'Iterative Deepening',         # [2] InSight
             'Depth-Limited Search',        # [3] Curiosity
             'Depth-First Search',          # [4] Phoenix
             'Uniform-Cost Search',         # [5] Opportunity
             'Breadth-First Search',        # [6] Spirit
             'Best-First Search'            # [7] Viking
            ]           

font = 'Protomolecule.otf'

author = 'Syed, Danial Haseeb'


# Title
titleFont = 'Protomolecule'
titleText = "Pathfinder"

byLine = Tex(r"\scshape by\\" + author, font_size=fontSize)

roverText = Tex(r"\scshape Selected Rover:", font_size=fontSize)
roverText.shift(UP/1.75).scale(0.75)


# Initialisation
def title(scene, index):
    with register_font(font):
        title = Text(titleText,
                     font=titleFont,
                     font_size=fontSize*2,
                     disable_ligatures=True)
        rover = Text(ROVER[index],
                     font=titleFont,
                     font_size=fontSize,
                     disable_ligatures=True)

    scene.play(Write(title), run_time=slow)
    scene.play(title.animate.to_edge(UP, LARGE_BUFF), run_time=slow)

    scene.play(Write(byLine), run_time=slow)

    logo = ImageMobject("logo.png").scale_to_fit_height(logoSize)
    logo.to_corner(DR)
    scene.play(FadeOut(byLine), FadeIn(logo), run_time=slow)

    scene.play(FadeIn(roverText, shift=UP), run_time=normal)
    scene.play(Write(rover), run_time=slow)

    group = VGroup()
    group.add(rover, roverText)

    algorithm = Tex(r"\scshape " + ALGORITHM[index], font_size=fontSize)
    scene.play(ReplacementTransform(group, algorithm), run_time=slow)

    group.add(title, algorithm)
    scene.play(FadeOut(group), run_time=slow)


def initialise(scene, roverIndex, startNode, goalNode):
    title(scene, roverIndex)
    createMaze(scene)
    markSpecialNode(scene, startNode)
    markSpecialNode(scene, goalNode)


# Maze
mNode = [[None for x in range(width)] for y in range(height)]
for y in range(height):
    for x in range(width):
        node = Square(nodeSize)
        location = Location(x, y)
        text = MathTex(str(location), font_size=axisSize).set_color(BLACK)
        node.add(text)
        if location.isObstacle():
            node.set_fill(gray, 1)
        mNode[y][x] = node

def createMaze(scene):
    maze = VGroup()
    for y in range(height):
        for x in range(width):
            maze += mNode[y][x]

    maze.arrange_in_grid(height, width, 0)

    for x in range(width):
        xLabel = Tex(str(x), font_size=axisSize)
        xLabel.next_to(mNode[0][x], UP, 0.2)
        maze += xLabel
    for y in range(height):
        yLabel = Tex(str(y), font_size=axisSize)
        yLabel.next_to(mNode[y][0], LEFT, 0.2)
        maze += yLabel

    scene.play(DrawBorderThenFill(maze), run_time=slow)
    scene.play(maze.animate.to_corner(), run_time=normal)


# Special Nodes
def markSpecialNode(scene, node):
    if (node == startNode):
        text = Tex(r"\textsc{Start:}", font_size=fontSize)
        colour = startColour
    else:
        text = Tex(r"\textsc{Goal:}", font_size=fontSize)
        colour = goalColour

    # Place text above first node in maze
    text.next_to(mNode[0][0], UP, nodeSize, LEFT)

    # Create given node
    x, y = node.location.x, node.location.y
    givenNode = mNode[y][x]

    # Create new node as copy of given node
    newNode = givenNode.copy()
    # Set special colour
    newNode.set_fill(colour, 1, 0)
    # Place new node next to text
    newNode.next_to(text, RIGHT)

    # Write text; place node alongside
    scene.play(Write(text), Create(newNode), run_time=normal)
    
    # Move new node to given node
    scene.play(newNode.animate.move_to(givenNode), run_time=normal)

    # Mark node as special
    mNode[y][x] = newNode.copy()
    scene.add(mNode[y][x])

    # Remove new node from maze since it's redundant now
    scene.remove(newNode)
    
    # Unwrite text
    scene.play(Unwrite(text), run_time=normal)
    scene.remove(text)


# Frontier
frontierText = Tex(r"\textsc{Frontier:}", font_size=fontSize)
frontierText.to_corner(UL)

def initialiseFrontier(scene, start) -> VGroup:
    scene.play(Write(frontierText))
    frontier = VGroup()
    addToFrontier(scene, frontier, start)
    return frontier

def rearrange(frontier):
    if len(frontier) == 0:
        return
    frontier.arrange_in_grid(1, len(frontier), 0)
    frontier.next_to(frontierText, RIGHT, nodeSize)

def addToFrontier(scene, frontier, node):
    x, y = node.location.x, node.location.y
    givenNode = mNode[y][x]
    scene.play(givenNode.animate.set_fill(frontierColour, 1, 0), run_time=normal)
    nodeToAdd = givenNode.copy()

    frontier += nodeToAdd
    rearrange(frontier)
    scene.remove(frontier[-1])

    copy = givenNode.copy()
    scene.play(copy.animate.move_to(frontier[-1]), run_time=normal)
    scene.add(frontier)
    scene.remove(copy)


# Current Node
currentNodeText = Tex(r"\textsc{Current Node:}", font_size=fontSize)
nSymbolText = Tex(r"\(n = \null\)", font_size=fontSize)

def setCurrentNode(scene, frontier, node, index) -> Square:
    # Create current node
    mCurrentNode = frontier[index].copy()

    scene.play(Circumscribe(frontier[index]), run_time=normal)

    # Remove current node from frontier
    frontier -= frontier[index]

    # Make copy of frontier (for animation later)
    frontierCopy = frontier.copy()

    # Animate current node next "n = "
    scene.play(mCurrentNode.animate.next_to(nSymbolText), run_time=normal)

    rearrange(frontier)
    scene.remove(frontier)

    x, y = node.location.x, node.location.y
    scene.play(TransformFromCopy(frontierCopy, frontier),
               mCurrentNode.animate.set_fill(currentNodeColour, 1, 0),
               mNode[y][x].animate.set_fill(currentNodeColour, 1, 0),
               Circumscribe(mNode[y][x]),
               run_time=slow)
    return mCurrentNode

def popFrontier(scene, frontier, node) -> Square:
    return setCurrentNode(scene, frontier, node, -1)

def dequeueFrontier(scene, frontier, node) -> Square:
    return setCurrentNode(scene, frontier, node, 0)


# Explored
def explore(scene, node):
    x, y = node.location.x, node.location.y
    scene.play(mNode[y][x].animate.set_fill(exploredColour, 1, 0), run_time=normal)


# Solution
def solve(scene, node):
    x, y = node.location.x, node.location.y
    scene.play(mNode[y][x].animate.set_fill(solutionColour, 1, 0), run_time=fast)