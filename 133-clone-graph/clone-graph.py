"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}

        def dfs(node):
            if not node:
                return 
            new_node = Node(node.val)
            visited[node] = new_node

            for neighbor in node.neighbors:

                if neighbor not in visited:
                    new_node.neighbors.append(dfs(neighbor))
                else:
                    new_node.neighbors.append(visited[neighbor])

            
            return new_node 
        
        new_node = dfs(node)
        return new_node


        