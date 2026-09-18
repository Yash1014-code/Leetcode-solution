class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        left = 0
        res = []
        n = len(s)
        map = {}
        for right in range(9,n):
            curr = s[left:right+1]
            if curr not in map :
                map[curr] = 1
            else :
                if map[curr] == 1:
                    res.append(curr[:])
                    map[curr] +=1
            left += 1
        return res                
        
