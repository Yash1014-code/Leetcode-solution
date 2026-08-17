class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        d=dict()
        res=[]
        for i in range(1,n+1):
            d[i]=0
        for i in range(0,n):
            d[nums[i]]+=1
        for key,value in d.items():
            if value==0:
                res.append(key)
        return res
