# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode | None) -> TreeNode | None:
        arr=[]
        self.inorder(root,arr)
        return self.build(arr,0,len(arr)-1)
    def build(self,arr,l,r):
        if l>r:
            return None
        mid = (l+r) // 2
        node = TreeNode(arr[mid])
        node.left = self.build(arr,l,mid-1)
        node.right = self.build(arr,mid+1,r)
        return node        
    def inorder(self,node,arr):
        if not node:
            return
        self.inorder(node.left,arr)
        arr.append(node.val)
        self.inorder(node.right,arr)    
