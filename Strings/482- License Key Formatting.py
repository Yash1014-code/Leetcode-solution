class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        ans=[]
        s = s.replace("-","").upper()
        for i in range(len(s),0,-k):
            start = max(0,i-k)
            ans.append(s[start:i])
        return "-".join(ans[::-1])
