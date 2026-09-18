class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=nums[-k]
        return n
