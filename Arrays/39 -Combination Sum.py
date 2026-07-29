class Solution:
    def solve(self,index,total,candidates,target,subset,result):
        if index>=len(candidates):
            return
        if  total==target:
            result.append(subset.copy())
            return
        if total>target:
            return
        subset.append(candidates[index]) 
        sum=total+candidates[index]
        self.solve(index,sum,candidates,target,subset,result)
        subset.pop()
        sum=total
        self.solve(index+1,sum,candidates,target,subset,result)        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        subset=[]
        self.solve(0,0,candidates,target,subset,result)
        return result
