class Solution:
    def __init__(self):
        self.chmap={
            "2":"abc",
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz',
            }
    def solve(self,index,digits,result,current):
        if index>=len(digits):
            result.append(current)
            return
        map=self.chmap.get(digits[index],"")

        for letter in map:
            self.solve(index+1,digits,result,current+letter)
            


    def letterCombinations(self, digits: str) -> List[str]:
        result=[]
        self.solve(0,digits,result,"")
        return result
        
        
