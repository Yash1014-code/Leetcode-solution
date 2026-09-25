# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.mx = 0

        def dfs(node):
            if not node:
                return (0, float('-inf'), float('inf'), 1)

            s1, lmin, lmax, v1 = dfs(node.left)
            s2, rmin, rmax, v2 = dfs(node.right)

            if (node.left and node.val <= node.left.val) or (lmax != float('inf') and node.val <= lmax):
                v1 = 0

            if (node.right and node.val >= node.right.val) or (rmin != float('-inf') and node.val >= rmin):
                v2 = 0

            if lmin == float('-inf'):
                lmin = node.val
            if rmax == float('inf'):
                rmax = node.val

            if v1 and v2:
                total = s1 + s2 + node.val
                self.mx = max(self.mx, total)
                return (total, lmin, rmax, 1)

            return (float('-inf'), -1, -1, 0)

        dfs(root)
        return self.mx     
        
