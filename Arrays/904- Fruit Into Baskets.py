class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        my_dict={}
        l=0
        r=0
        maxi=0
        n=len(fruits)
        for r in range(0,n):
            my_dict[fruits[r]]=my_dict.get(fruits[r],0)+1
            if len(my_dict)>2:
                my_dict[fruits[l]]-=1
                if my_dict[fruits[l]]==0:
                    del my_dict[fruits[l]]
                l+=1
            if len(my_dict)<=2:
                maxi=max(maxi,r-l+1)
            r+=1
        return maxi
              
        
