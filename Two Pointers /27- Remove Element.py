class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        i=0
        j=0
        while i<n:
            if val!=nums[i]:
                nums[j]=nums[i]
                j+=1 
            i+=1
        return j        
