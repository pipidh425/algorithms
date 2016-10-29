# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):  # O(mn) time, m is the number of nodes, n is the longest path, O(n) space
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        cur_list = []
        res = [0]
        
        def pathHelper(root, sum, cur_list, res):
            if root is None:
                return
            cur_list.append(root.val)
            subtotal = 0
            for i in range(len(cur_list) - 1, -1, -1):
                subtotal += cur_list[i]
                if subtotal == sum:
                    res[0] += 1
                    
            pathHelper(root.left, sum, cur_list, res)
            pathHelper(root.right, sum, cur_list, res)
            del cur_list[-1]
            
        pathHelper(root, sum, cur_list, res)
            
        return res[0]
