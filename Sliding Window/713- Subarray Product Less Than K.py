class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1 :
            return 0
        l = 0
        res = 0
        pro = 1
        n = len(nums)
        for r in range(n):
            pro *= nums[r]
            while pro >= k :
                pro//=nums[l]
                l+=1
            res += (r-l)+1
        return res        
