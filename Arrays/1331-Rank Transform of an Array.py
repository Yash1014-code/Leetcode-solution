class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s=sorted(arr)
        unique=[]
        for x in s:
            if not unique or unique[-1]!=x:
                unique.append(x)
        for i in range(0,len(arr)):
            arr[i]=bisect_left(unique,arr[i])+1
        return arr            
