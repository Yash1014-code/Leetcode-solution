class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i  in range(n):
            num = i+1
            if n%num == 0 :
                count += nums[num-1]**2
        return count  
