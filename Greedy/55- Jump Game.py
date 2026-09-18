class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        ind=0
        for i in range(0,n):
            if i>ind:
                return False
            ind=max(ind,i+nums[i]) 
        return True       
