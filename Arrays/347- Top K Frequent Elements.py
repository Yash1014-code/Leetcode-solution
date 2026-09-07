class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m=len(nums)
        dic={}
        for n in nums:
            dic[n]=1+dic.get(n,0)
        freq=[[] for _ in range(m+1)]
        for n,f in dic.items():
            freq[f].append(n)
        res=[]
        for i in range (len(freq)-1,-1,-1):
            for n in freq[i]:
                res.append(n) 
                if len(res)==k:
                    return res
