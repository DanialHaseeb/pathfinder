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
"""
from collections import deque
from pickletools import UP_TO_NEWLINE
from shelf import *

# [3]
class Curiosity(Scene):
    """Depth-Limited Search."""
    def construct(self):
        initialise(self, 3, startNode, goalNode)

        explored = set()
        def depthLimitedSearch(node, limit):
            if ((node in explored) or (limit == 0)):
                return 'cutoff'
            
            if (node == goalNode):
                return node.path()

            explored.add(node)

            cutOff = False

            for child in node.expand():
                print("Parent:", node)
                print("Child:", child)
                result = depthLimitedSearch(child, limit-1)

                if   result == 'cutoff':
                     cutOff = True
                elif result is not None:
                     
                     return result

            print()
            print("**********")
            return 'cutoff' if cutOff else None

        depthLimitedSearch(startNode, 4)

        



# [4]
class Phoenix(Scene):
    """Depth-First Search."""
    def construct(self):
        initialise(self, 4, startNode, goalNode)


        # Frontier
        frontier  = [startNode]
        mFrontier = initialiseFrontier(self, startNode)


        # Current Node
        currentNodeText.next_to(mNode[0][width-1], buff=nodeSize)
        nSymbolText.next_to(currentNodeText, DOWN, nodeSize, LEFT)
        self.play(Write(currentNodeText), Write(nSymbolText), run_time=normal)

        currentNode  = frontier.pop()
        mCurrentNode = popFrontier(self, mFrontier, currentNode)


        # Explored Nodes
        explored = set()


        # Depth-First Search
        while frontier is not None:
            if (currentNode == goalNode):
                self.play(mCurrentNode.animate.set_fill(goalColour, 1, 0),
                          Flash(mNode[goal[1]][goal[0]], color=goalColour),
                          mNode[goal[1]][goal[0]].animate.set_fill(goalColour,
                                                                   1, False),
                          run_time=normal)
                for node in currentNode.path():
                    solve(self, node)
                break
            
            explored.add(currentNode)
            explore(self, currentNode)

            for child in currentNode.expand():
                if (child not in frontier) and (child not in explored):
                    frontier.append(child)
                    addToFrontier(self, mFrontier, child)
            
            currentNode  = frontier.pop()
            mCurrentNode = popFrontier(self, mFrontier, currentNode)


# [6]
class Spirit(Scene):
    """Breadth-First Search."""
    def construct(self):
        initialise(self, 6, startNode, goalNode)


        # Frontier
        frontier  = [startNode]
        frontier  = deque(frontier)
        mFrontier = initialiseFrontier(self, startNode)


        # Current Node
        currentNodeText.next_to(mNode[0][width-1], buff=nodeSize)
        nSymbolText.next_to(currentNodeText, DOWN, nodeSize, LEFT)
        self.play(Write(currentNodeText), Write(nSymbolText), run_time=normal)

        currentNode  = frontier.popleft()
        mCurrentNode = dequeueFrontier(self, mFrontier, currentNode)


        # Explored Nodes
        explored = set()


        # Breadth-First Search
        while frontier is not None:
            if (currentNode == goalNode):
                self.play(mCurrentNode.animate.set_fill(goalColour, 1, 0),
                          Flash(mNode[goal[1]][goal[0]], color=goalColour),
                          mNode[goal[1]][goal[0]].animate.set_fill(goalColour,
                                                                   1, False),
                          run_time=normal)
                for node in currentNode.path():
                    solve(self, node)
                break

            explored.add(currentNode)
            explore(self, currentNode)

            for child in currentNode.expand():
                if (child not in frontier) and (child not in explored):
                    frontier.append(child)
                    addToFrontier(self, mFrontier, child)
            
            currentNode  = frontier.popleft()
            mCurrentNode = dequeueFrontier(self, mFrontier, currentNode)