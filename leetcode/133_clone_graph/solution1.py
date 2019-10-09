"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
from collections import deque


class Solution:
    def cloneGraph(self, node):
        root = node
        if node is None:
            return node
        nodes = self.get_nodes(node)
        mapping = {}
        for node in nodes:
            mapping[node] = Node(node.val, [])
        for node in nodes:
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)
        return mapping[root]

    def get_nodes(self, node):
        queue = deque([node])
        result = set([node])
        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors:
                if neighbor not in result:
                    result.add(neighbor)
                    queue.append(neighbor)
        return result
