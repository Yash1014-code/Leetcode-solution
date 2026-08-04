class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mini=min(nums)
        maxi=max(nums)
        res=[]
        while mini<maxi:
            if mini not in nums:
                res.append(mini)
            mini+=1
        return res        
