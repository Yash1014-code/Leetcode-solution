class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        dict1=dict()
        for i in range(1,n+1):
            dict1[i]=0
        for num in nums:
            dict1[num]+=1
        for key,value in dict1.items():
            if value>1:
                n1=key
            if value==0:
                n2=key
        return [n1,n2]               

            
