class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        r_sum=0
        l_sum=0
        maxi=0
        if n==k:
            return sum(cardPoints)
        for i in range(0,k): 
            l_sum+=cardPoints[i]
        maxi=l_sum
        r=n-1
        for i in range(k-1,-1,-1):
            l_sum-=cardPoints[i]
            r_sum+=cardPoints[r]
            r-=1
            maxi=max(maxi,l_sum+r_sum)
        return maxi        
