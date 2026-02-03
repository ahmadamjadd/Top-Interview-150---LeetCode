"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def check(self, grid: List[List[int]]):
        if all(cell == grid[0][0] for row in grid for cell in row):
            return True
        return False

    def construct(self, grid: List[List[int]]) -> 'Node':
        node = Node()
        isSame = self.check(grid)
        if isSame:
            node.isLeaf = 1
            node.val = grid[0][0]
            node.topLeft = None
            node.topRight = None
            node.bottomLeft = None
            node.bottomRight = None
            return node
        node.isLeaf = 0
        rows = len(grid) // 2

        top_half = grid[:rows]
        bottom_half = grid[rows:]

        node.topLeft = self.construct([row[:rows] for row in top_half])
        node.topRight = self.construct([row[rows:] for row in top_half])
        node.bottomLeft = self.construct([row[:rows] for row in bottom_half])
        node.bottomRight = self.construct([row[rows:] for row in bottom_half])
        return node


       
        
