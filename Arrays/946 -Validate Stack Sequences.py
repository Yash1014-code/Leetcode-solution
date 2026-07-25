class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n=len(pushed)
        m=len(popped)
        s=[]
        j=0
        for i in range(0,n):
            s.append(pushed[i])
            while s and s[-1]==popped[j]:
                s.pop()
                j+=1       
        if s:
            return False
        else:
            return True
