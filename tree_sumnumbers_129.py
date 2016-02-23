# https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.total = 0
        self.dfs(root, str(root.val))
        return self.total
        
    def dfs(self, root, sum1):
        if not root.left and not root.right:
            self.total += int(sum1)
        if root.left:
            self.dfs(root.left, '{}{}'.format(sum1, root.left.val))
        if root.right:
            self.dfs(root.right, '{}{}'.format(sum1, root.right.val))
