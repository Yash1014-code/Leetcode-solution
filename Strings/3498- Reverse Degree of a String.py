class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0 
        for i,c in enumerate(s):
            reverse_s = 26 - (ord(c)-ord('a'))
            pos = i+1
            total += pos*reverse_s
        return total    
