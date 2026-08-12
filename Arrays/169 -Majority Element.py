class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_list={}
        for i in range(0,len(nums)):
            hash_list[nums[i]] = hash_list.get(nums[i],0)+1
        for key in hash_list.keys():
            if hash_list[key] > len(nums) // 2:
                return key
