class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = dict()
        for c in text :
            if ( c=='b' or c=='a' or c=='l' or c=='o' or c=='n'):
                freq[c] = freq.get(c,0)+1
       
        b = freq.get('b',0)
        a = freq.get('a',0)
        l = freq.get('l',0)//2
        o = freq.get('o',0)//2
        n = freq.get('n',0)

        return min(b,a,l,o,n)
        
