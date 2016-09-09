# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if node is None:
            return None
            
        node_map = {} # mark whether a node has been cloned
        return self.clone(node, node_map)
        
    # O(N) time, O(N) space
    def clone(self, node, node_map):
        if node.label in node_map:
            return node_map[node.label]
            
        copy = UndirectedGraphNode(node.label)
        node_map[copy.label] = copy
        copy.neighbors = [self.clone(neighbor, node_map) for neighbor in node.neighbors]
        return copy
