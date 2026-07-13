class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candie=max(candies)
        temp=0
        for i in range(0,len(candies)):
            temp=candies[i]+extraCandies
            if temp>=max_candie:
                candies[i]=True
            else:
                candies[i]=False
            temp=0        
        return candies
