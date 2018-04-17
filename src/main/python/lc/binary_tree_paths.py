# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        all_paths = []
        cur_path = []
        self.traverseTree(root, cur_path, all_paths)
        return all_paths
        
    def traverseTree(self, node, cur_path, all_paths):
        if node is None:
            return
        cur_path.append(str(node.val))
        if node.left is None and node.right is None:
            path = "->".join(cur_path)
            all_paths.append(path)
        else:
            if node.left is not None:
                self.traverseTree(node.left, cur_path, all_paths)
            if node.right is not None:
                self.traverseTree(node.right, cur_path, all_paths)
        del cur_path[-1]
            
            
        
