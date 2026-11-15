class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        mod = 10**9 + 7
        odd = even = ans = 0
        for i in arr:
            if i%2 == 1:
                odd, even = even+1, odd
            else:
                even+=1

            ans = ans+odd
        return ans%mod     
        
