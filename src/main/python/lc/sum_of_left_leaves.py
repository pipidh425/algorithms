# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def sumHelper(self, node, is_left):
        if node is None:
            return 0
        elif node.left is None and node.right is None and is_left:
            return node.val
        else:
            return self.sumHelper(node.left, True) + self.sumHelper(node.right, False)
        
         
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.sumHelper(root, False)
        
