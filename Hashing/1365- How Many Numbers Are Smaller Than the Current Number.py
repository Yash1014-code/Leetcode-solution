class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[]
        for i in range(0,n):
            count=0
            for j in range(0,n):
                if nums[i]>nums[j]:
                    count+=1
                if nums[i]<=nums[j]:
                    continue
            res.append(count)  
        return res              
