class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n= len(gain)
        ans = [0]*(n+1)
        for i in range(0,n):
            ans[i+1] = ans[i]+gain[i]
        return max(ans)
