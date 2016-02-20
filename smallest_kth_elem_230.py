# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.count = k
        return self.inorder(root)
        
    def inorder(self, root):
        if root:
            success = self.inorder(root.left)
            if success is None:
                self.count -= 1
                if self.count == 0:
                    success = root.val
                if success is None:
                    success = self.inorder(root.right)
            return success
