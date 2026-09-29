# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: TreeNode | None, target: int) -> TreeNode | None:
        if not root:
            return
        left = self.removeLeafNodes(root.left,target)
        right = self.removeLeafNodes(root.right,target)

        if not left and not right and root.val == target:
            return 
        return root 
