class Solution:
    def checkString(self, s: str) -> bool:
        count=0
        for i in range(len(s)):
            if s[i]=='b':
                count+=1
            elif count>0 and s[i]=='a':
                return False
        return True    
        
