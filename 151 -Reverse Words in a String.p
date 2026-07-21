class Solution:
    def reverseWords(self, s: str) -> str:
        temp=""
        sample=""
        
        for num in s:
            if num!=" ":
                temp+=num
            elif num==" " and temp:
                sample=temp+" "+sample
                temp=""
            else:
                continue  
        if temp:
            sample=temp+" "+sample          
        return sample.strip()
