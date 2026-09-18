class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        n=len(s)
        for i in range(0,n):
            if s[i]=='('or s[i]=='['or s[i]=='{':
                stack.append(s[i])
            else:
                if not stack:
                    return False
                t=stack.pop() 
                if s[i]==')'and t!='(':
                    return False
                if s[i]==']' and t!='[':
                    return False
                if s[i]=='}' and t!='{':
                    return False
        return len(stack)==0                   
