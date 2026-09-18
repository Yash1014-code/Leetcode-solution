class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        l = 0
        res=0
        ans=0
        for r in range(0,len(arr)):
            res += arr[r]
            while r-l+1 > k:
                res-=arr[l]
                l+=1
            if r-l+1==k and res>=(threshold*k):
                ans+=1
        return ans        
