class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m = max(nums)
        n = len(nums)
        count = 0
        for num in nums:
            count += (m- num)
        return count  
