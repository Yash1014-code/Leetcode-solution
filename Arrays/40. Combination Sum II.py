class Solution:
    def solve(self,index,total,candidates,subset,result):
        if total==0:
            result.append(subset.copy())
            return
        for i in range(index,len(candidates)):
            if i>index and candidates[i]==candidates[i-1]:
                continue
            if candidates[i] > total:
                break        
            subset.append(candidates[i])
            sum=total-candidates[i]
            self.solve(i+1,sum ,candidates,subset,result)
            subset.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result=[]
        subset=[]
        self.solve(0,target,candidates,subset,result)
        return result
