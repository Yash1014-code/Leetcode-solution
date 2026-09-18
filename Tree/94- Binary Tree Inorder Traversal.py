# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.result=[]
        self.solve(root)
        return self.result
    def solve(self,root):    
        if not root:
            return 0
        self.solve(root.left)
        self.result.append(root.val)
        self.solve(root.right)
        return self.result


        
