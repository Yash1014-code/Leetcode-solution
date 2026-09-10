class Solution:
    def pivotIndex(self, nums):
        n=len(nums)
        left=0
        right=0
        for i in range (n):
            left = sum(nums[:i])
            right=sum(nums[i+1:])
            if left == right:
                return i
    
        return -1                 


        
       
