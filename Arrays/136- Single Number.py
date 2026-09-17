class Solution:
    def singleNumber(self, nums):
        n_set = set()
        for i in range(len(nums)):
            if nums[i] not in n_set:
                n_set.add(nums[i])
            else: 
                n_set.remove(nums[i])
        return n_set.pop()          
