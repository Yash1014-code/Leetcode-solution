# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: TreeNode | None) -> int:
        self.best = 0
        MOD = 10**9 + 7
        def total_sum(node):
            if not node:
                return 0
            return node.val+total_sum(node.left)+total_sum(node.right) 
        total = total_sum(root)
        
        def Sum(node):
            if not node:
                return 0
            s = node.val + Sum(node.left) + Sum(node.right)
            self.best = max(self.best, s*(total-s))
            return s
        Sum(root)
        return self.best % MOD  
