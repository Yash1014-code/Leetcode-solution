class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*n
        pre=1
        for i in range(0,n):
            res[i]=pre
            pre*=nums[i]
        suff=1
        for i in range(n-1,-1,-1):
            res[i]*=suff
            suff*=nums[i]
        return res
